import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from skopt import gp_minimize
from skopt.space import Real, Integer
from skopt.utils import use_named_args

# Load the dataset
df = pd.read_csv('/Users/kellerrajashree/Desktop/Maze_Game/drug200.csv')

# Data preprocessing
df.fillna(method='ffill', inplace=True)  # Handle missing values
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])  # Encode 'Sex' column

# Define features and target variable
X = df[['Age', 'Sex', 'Blood Pressure', 'Cholesterol', 'Na/K Ratio']]
y = df['Drug Type']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the search space for hyperparameters
search_space = [
    Integer(5, 100, name='n_estimators'),  # Number of trees in the forest
    Real(0.01, 1.0, name='max_features'),   # The number of features to consider when looking for the best split
]

# Define the objective function for Bayesian Optimization
@use_named_args(search_space)
def objective_function(n_estimators, max_features):
    model = RandomForestClassifier(n_estimators=n_estimators, max_features=max_features, random_state=42)
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Make predictions
    return -accuracy_score(y_test, y_pred)  # Return negative accuracy for minimization

# Perform Bayesian Optimization
result = gp_minimize(
    func=objective_function, 
    dimensions=search_space,
    n_calls=30,  # Number of calls to the objective function
    random_state=42
)

# Get the best hyperparameters
best_n_estimators = result.x[0]
best_max_features = result.x[1]

print(f"Best Hyperparameters: n_estimators={best_n_estimators}, max_features={best_max_features}")

# Train the model with the best hyperparameters
best_model = RandomForestClassifier(n_estimators=best_n_estimators, max_features=best_max_features, random_state=42)
best_model.fit(X_train, y_train)

# Make predictions
y_pred = best_model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

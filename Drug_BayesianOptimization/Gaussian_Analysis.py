import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from skopt import gp_minimize
from skopt.space import Real, Integer
from skopt.utils import use_named_args
from skopt.plots import plot_convergence
import matplotlib.pyplot as plt

# Load example dataset (Iris dataset)
data = load_iris()
X, y = data.data, data.target

# Define the search space for RandomForest hyperparameters
search_space = [
    Integer(10, 200, name='n_estimators'),           # Number of trees
    Integer(1, 10, name='max_depth'),                # Depth of trees
    Real(0.1, 1.0, name='max_features')              # Number of features considered for best split
]

# Define the objective function for Bayesian optimization
@use_named_args(search_space)
def objective_function(**params):
    # Unpack hyperparameters
    n_estimators = params['n_estimators']
    max_depth = params['max_depth']
    max_features = params['max_features']
    
    # Create a RandomForestClassifier with the given hyperparameters
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        max_features=max_features,
        random_state=42
    )
    
    # Evaluate model performance using cross-validation
    # We want to maximize accuracy, so we take the negative for minimization
    score = -np.mean(cross_val_score(model, X, y, cv=5, scoring='accuracy'))
    
    return score

# Perform Bayesian Optimization
def bayesian_optimization(search_space, objective_function, n_calls=30, n_initial_points=10):
    """
    Perform Bayesian Optimization to find the best hyperparameters.
    
    Args:
    search_space (list): The hyperparameter search space.
    objective_function (function): The objective function to minimize (negative accuracy).
    n_calls (int): Number of function evaluations.
    n_initial_points (int): Number of initial random samples.

    Returns:
    result: The optimization result with the best hyperparameters.
    """
    print("Starting Bayesian Optimization...")
    
    result = gp_minimize(
        func=objective_function,       # The function to minimize
        dimensions=search_space,       # The search space
        n_calls=n_calls,               # Number of function evaluations
        n_initial_points=n_initial_points,  # Random samples before optimization
        acq_func='EI',                 # Acquisition function (Expected Improvement)
        random_state=42                # For reproducibility
    )
    
    print(f"Best hyperparameters: {result.x}")
    print(f"Best negative accuracy (minimized): {result.fun}")
    
    return result

# Run Bayesian Optimization
if __name__ == "__main__":
    result = bayesian_optimization(search_space, objective_function)
    
    # Plot the convergence plot
    plot_convergence(result)
    plt.title("Convergence Plot")
    plt.show()
    
    # Best hyperparameters found
    print("Optimized Hyperparameters:")
    print(f"n_estimators: {result.x[0]}")
    print(f"max_depth: {result.x[1]}")
    print(f"max_features: {result.x[2]}")

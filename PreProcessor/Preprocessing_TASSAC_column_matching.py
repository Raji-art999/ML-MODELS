import csv


csv_file1 = "/Users/sundaramrajashree/PycharmProjects/Webscraping/MAT4_structure.csv"


csv_file2 = "/Users/sundaramrajashree/PycharmProjects/Webscraping/MATvariables.csv"


output_csv_file = "MAT4structure.csv"


data_dict = {}
with open(csv_file2, 'r', newline='') as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        data_dict[row[0]] = row[1]


with open(csv_file1, 'r', newline='') as file1, open(output_csv_file, 'w', newline='') as output_file:
    reader1 = csv.reader(file1)
    writer = csv.writer(output_file)
    for i, row in enumerate(reader1):
        key = row[0]
        if key in data_dict:
            matched_value = data_dict[key]
            if i == 0:
                row.insert(1, "Matched Value")
            else:
               
                row.insert(1, matched_value)
        writer.writerow(row)

print(f'Merged data saved to {output_csv_file}')
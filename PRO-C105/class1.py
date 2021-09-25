import csv
with open("class1.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
total_marks = 0
total_entries = len(file_data)
for marks in file_data:
    total_marks +=
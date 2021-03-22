import csv

with open('src/report.csv', 'r') as file:
    reader = csv.reader(file)
    reader = list(reader)
    header = reader[0]
    for row in reader[1:]:
        res = dict(zip(header, row)) # => [(Id, 543), (Name, Benajmin), ..]
        # print(header)
        print(res)

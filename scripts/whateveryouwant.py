import csv

with open('PaulinaDataset.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data[0])
#print(len(data))
for row in data[1:]:
    description = row[3]
    if "water spider" in description:
        print(row)
    elif "waterspider" in description:
        print(row)
    elif "pallet" in description:
        print(row)

import csv
import json

with open("leedbuildings.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    building_rows = [row for row in reader]

headers = building_rows.pop(0)

projectTypeIndex = headers.index('ProjectTypes')

count = 0

counts = {
    "Retail": 0
}

for value in building_rows:
    
    # ["Commercial Buildings", "Retail", "other building type..."]
    projectTypes = value[projectTypeIndex].split(",")

    for projectType in projectTypes:
        projectType = projectType.strip()
        if projectType not in counts:
            counts[projectType] = 0
        counts[projectType] += 1
    # print(value[projectTypeIndex])

list_of_building_counts = sorted(
    counts.items(),
    key=lambda key: key[1],
    reverse=True
)

for building_type in list_of_building_counts:
    print(building_type)
    count += 1
    if count > 5:
        break

# print(json.dumps(counts, indent=4))

# print(projectTypeIndex)
# print(building_rows[0])
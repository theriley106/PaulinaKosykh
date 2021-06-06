import csv
import pgeocode

converter = pgeocode.Nominatim('us')

with open("leedbuildings.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    building_rows = [row for row in reader]

headers = building_rows.pop(0)

zipcodeIndex = headers.index('Zipcode')

count = 0

for row in building_rows:
    try:
        zipCode = row[zipcodeIndex]

        info = converter.query_postal_code(zipCode)
        long_lat = "{}, {}".format(info.longitude, info.latitude)
        if 'nan' not in long_lat:
            print(long_lat)
    except:
        pass
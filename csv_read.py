import csv

csv_file = open("data/health_inspection_chi_sample.csv")
reader = csv.reader(csv_file)
# csv.reader returns a lazy iterator

# first line read is the header
headers = next(reader)

# next lines are data to be read
line = next(reader)

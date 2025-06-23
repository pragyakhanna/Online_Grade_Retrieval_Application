import csv
from hash_code import hash_credentials

def Authenticate(compare):
     found = []
     with open('Database.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    line_count += 1
                    combined_input = row[0] + ":" + row[1]
                    if compare == hash_credentials(combined_input):
                        found = [f'Last Name: {row[2]}, First Name: {row[3]}, Midterm : {row[4]}, Lab 1: {row[5]}, Lab 2: {row[6]}, Lab 3: {row[7]}, Lab 4: {row[8]}']
     return found
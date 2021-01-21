import csv

# Write file.
with open('file.csv', 'w', newline='') as csvfile:
    
    csv_writer = csv.writer(csvfile, delimiter=';')
    csv_writer.writerow(['titile1', 'titile2', 'titile3', 'titile4', 'titile5'])
    csv_writer.writerow(['column1', 'column2', 'column3', 'column4', 'column5'])


# Read file.
with open('file.csv', 'r', newline='') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=';')
    for line in csv_reader:
        print(';'.join(line))


# Read to Dict
with open('file.csv', 'r', newline='') as csvfile:
     
     csv_reader = csv.DictReader(csvfile, delimiter=';')
     for row in csv_reader:
         print(row)


# Write to Dict
with open('file.csv', 'w', newline='') as csvfile:
    
    fieldnames = ['title1', 'title2', 'title3', 'title4', 'title5']
    csv_writer = csv.DictWriter(csvfile, delimiter=';' ,fieldnames=fieldnames)

    dict_model = {'title1':'column1', 'title2':'column2', 'title3':'column3', 'title4':'column4', 'title5':'column5'}

    csv_writer.writeheader()
    csv_writer.writerow(dict_model)
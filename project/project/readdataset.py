
import numpy as np

# using loadtxt()
arr = np.loadtxt("Train.csv",
                 delimiter=",", dtype=str)

lis=[1, 26, 51, 76, 101, 126, 151, 176, 201, 226]
rows=[]
lab=[]
ii=0
for i in arr:
    print(i)

    row=[]
    row.append(list(i)[lis[0]])
    row.append(list(i)[lis[1]])
    row.append(list(i)[lis[2]])
    row.append(list(i)[lis[3]])
    row.append(list(i)[lis[4]])
    row.append(list(i)[lis[5]])
    row.append(list(i)[lis[6]])
    row.append(list(i)[lis[7]])
    row.append(list(i)[lis[8]])
    row.append(list(i)[lis[9]])
    if ii==0:
        lab=row
    else:
        rows.append(row)
    ii=ii+1




import csv

# field names
fields =lab

# data rows of csv file


# name of csv file
filename = "landslide_dataset.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)


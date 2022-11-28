import MySQLdb
import datetime
import csv
import env

connection = MySQLdb.connect(
        host='localhost',
        user=env.USER,
        passwd=env.PASSWORD,
        db=env.DB)
cursor = connection.cursor()

cursor.execute("SELECT * FROM events where type = 1")

myresult = cursor.fetchall()

datedata = {}

for x in myresult:
    if str(x[4].strftime("%Y-%m-%d")) in datedata:
        datedata[x[4].strftime("%Y-%m-%d")] += 1
    else:
        datedata[x[4].strftime("%Y-%m-%d")] = 1

fieldNames = ['date', 'numbers']

with open('rawdata.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in datedata.items():
        writer.writerow([key,value])

datetdata2base = {}
datedata2 = {}

for x in myresult:
    if(x[4].strftime("%Y-%m-%d")) in datetdata2base:
        if x[1] not in datetdata2base[x[4].strftime("%Y-%m-%d")]:
            datetdata2base[x[4].strftime("%Y-%m-%d")].append(x[1])
    else:
        datetdata2base[x[4].strftime("%Y-%m-%d")] = [x[1]]

for key, value in datetdata2base.items():
    datedata2[key] = len(value)

with open('uniquedata.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key, value in datedata2.items():
        writer.writerow([key,value])

# print(datedata2)
# print(datedata)
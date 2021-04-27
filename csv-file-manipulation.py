import csv

file = open('example.csv')
fileReader = csv.reader(file)

print(fileReader)


### Human Readable Form 

file = open('example.csv')
fileReader = csv.reader(file)

data = list(fileReader)
print(data)

print(data[0][2])


#### LOOP USING ## 
### ROW WISE PRINTING 

for row in fileReader:
    print('Row no = '+str(fileReader.line_num)+" "+ str(row))
    



## CSN FILE WRITING

outpurFile = open('out.csv', 'w', newline='')
outputWriter = csv.writer(outpurFile)
outputWriter.writerow(['1', '2', '3', '4'])
outputWriter.writerow(['15', '24', '33', '42'])

outputWriter.close()

#### TO SEparate data by any other symbol use delimeter

outpurFile = open('out.csv', 'w', newline='')
outputWriter = csv.writer(outpurFile,delimiter = "/")
outputWriter.writerow(['1', '2', '3', '4'])
outputWriter.writerow(['15', '24', '33', '42'])

outputWriter.close()

### APPENDING 

outpurFile = open('out.csv', 'a', newline='')
outputWriter = csv.writer(outpurFile,delimiter = "/")
outputWriter.writerow(['1', '2', '3', '4'])
outputWriter.writerow(['15', '24', '33', '42'])

outputWriter.close()



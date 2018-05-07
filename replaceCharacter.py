import csv
import string
import pickle

input_file = open('AccreditationByHep.csv', 'r')
output_file = open('AccreditationByHepModified.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)
specials = "'"

for line in data:
    line = str(line)
    new_line = str.replace(line,specials,"\'")
    #new_line = str.translate(str.maketrans({"'":None}))# but it's a string
    writer.writerow(new_line.split(','))


input_file.close()
output_file.close() 

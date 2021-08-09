# calculate the average of float number after the words "X-DSPAM-Confidence : "
file_name = input('Enter the file name : ')
#create an object
f = open(file_name)
#variable to put the amount of data containing the word we are looking for
n = 0
#variable to sum all of the float we get from the words
total_float = 0

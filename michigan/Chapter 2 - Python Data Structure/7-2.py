# calculate the average of float number after the words "X-DSPAM-Confidence : "
file_name = input('Enter the file name : ')
#create an object
f = open(file_name)
#count the amount of lines
n = 0 
#sum all float after XDSPAM
total_of_float = 0 
#convert n to flot because it will be used as a denominator for average calculation
nf = float(n)
for line in f :
    if not line.startswith('X-DSPAM-Confidence:') : continue
    n = n + 1
    #take the number after comma
    xDSPAM = line[line.find('0') : ]
    #convert xDSPAM to float
    xDSPAM_float = float(xDSPAM)
    #sum all the float we get from scanning the file
    total_of_float = total_of_float + xDSPAM_float
xDSPAM_float_average = total_of_float/n
print('Average spam confidence:', xDSPAM_float_average)



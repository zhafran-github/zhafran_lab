fname = input("Enter file name: ")
f = open(fname)
#create a string
poemf = f.read()
#convert the string into list with splitted words
poem = poemf.split()
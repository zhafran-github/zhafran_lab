fname = input("Enter file name: ")
f = open(fname)
#create a string
poemf = f.read()
#convert the string into list with splitted words
poem = poemf.split()

a=[]

for word in poem :
    if word in a :
        continue
    else :
         a.append(word)

a.sort()
print(a)
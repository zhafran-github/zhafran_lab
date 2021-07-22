#create flag
largest = -1
smallest = None

#read number from a user
x= input('Enter Number:')

#keep asking input until user submit the word 'done'
while x != 'done' :
    #using try and except for error handling
    try :
        if x == 'done' :
            break
        else :
            k = int(x)
            #finding maximum value
            if k > largest :
                largest = k
            #finding minimum value
            if smallest is None :
                smallest = k
            elif k < smallest :
                smallest = k
            x = input('Enter Number:')
    #error handling in case user submit input other than number or the word 'done'
    except:
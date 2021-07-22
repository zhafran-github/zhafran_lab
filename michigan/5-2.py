# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below. 

# Desired Ouput
# Invalid Input  
# Maximum is 10 
# Minimum is 2 

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
        print('Invalid input')
        x = input('Enter Number:')

#print max and min
print('Maximum is', largest)
print('Minimum is', smallest)
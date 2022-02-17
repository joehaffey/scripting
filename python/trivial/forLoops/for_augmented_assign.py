'''
file name for_augmented_assignment.py
created by joe haffey on wednesday november 10, 2021 at 2:05 pm
this program demonstrates python's augmented assignment operators in a for loop.  
the program asks the user to input start, stop, and step values.  then it asks for another number and applies the augmented assignment operators.  
'''

#the number that will augment the values
num1 = int(0)

#the loop values
start_value = int(0)   #for the starting value
stop_value = int(0)  #for the ending value
step_value = int(0)  #for the value of the increment

#gets the numbers from the user
#for num1
num1 = int(input('enter a number: '))
start_value = int(input('enter the starting value: '))
stop_value = int(input('enter the ending value: '))
step_value = int(input('enter the increment value: '))

#the loop
for num1 in range(start_value, stop_value, step_value):
	#add assigns num1 and step_value
	num1 += step_value
	print('the value of num1 is: ', num1)


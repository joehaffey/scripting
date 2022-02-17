"""
file name math_ops.py
created by joehaffey on saturday october 2, 2021 at 11:36 am
this file demonstrates the basic math operators in python.  it asks the user to input 2 numbers then performs the basic calculations on them.  
"""

#these 2 lines ask the user to input the number
num1 = int(input('Enter a number: '))       #the 1st number
num2 = int(input('Enter another number: ')) #the 2nd number

#the calculations
sum = num1 + num2       #for addition
diff = num1 - num2      #for subtraction
prod = num1 * num2      #for multiplication
quot = num1 / num2      #for division
mod = num1 % num2       #for modulus
exp = num1 ** num2      #exponentiation
floor_div = num1 // num2  #floor division

#prints the results
print('The sum of ', num1, 'and', num2, 'is: ', sum)
print('The difference of ', num1, 'and', num2, 'is: ', diff)
print('The product of ', num1, 'and', num2, 'is: ', prod)
print('The quotient of ', num1, 'and', num2, 'is: ', quot)
print('The modulus of ', num1, 'and', num2, 'is: ', mod)
print(num1, 'raised to the power of ', num2, 'is', exp)
print('Floor division of ', num1, 'by ', num2, 'is ', floor_div)
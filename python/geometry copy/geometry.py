'''
file name geometry.py
created by joe haffey on wednesday january 12, 2022 at 2:38 pm
this program demonstrates pre-defined formulae in python.  it asks the user for various dimensions of geometric shapes and computes the perimeter/circumference, area, and unknown angles.
'''

#built in module imports
import sys
import math

#circle definition
#{{{ 
def func_circles():
	#asks to choose the operation they want
	print('Press the number next to the operation you want: ')
	print('1: Find Diameter')
	print('2: Find Area')
	print('3: Find Circumference')
	
	#gets operation choice from the user
	select_circle_operation = int(input(">"))
	
	#tests to see what the user chose
	
	#if the user chose diameter
	if select_circle_operation == 1:
		#gets the radius from the user
		circle_radius = float(input('Enter the radius of the circle: '))
		
		#finds the diameter
		circle_diameter = 2 * circle_radius
		
		#prints the resulst
		print('Diameter = 2 * radius')
		print('Diameter = 2 *', circle_radius)
		print('Diameter =', circle_diameter)
		
	#if the user chose area
	if select_circle_operation == 2:
		#local variable for pi
		pi = 3.14159
	
		#gets the radius from the user
		circle_radius = float(input('Enter the radius of the circle: '))
		
		#finds the area
		circle_area = pi * (circle_radius **2)
		
		#prints the result
		print('Area = pi * radius ** 2')
		print('Area = pi *', circle_radius, '** 2')
		print('Area =', circle_area)
		
	#if the user chose circumference
	
	#local variable for pi
	pi = 3.14159
	
	if select_circle_operation == 3:
		#gets the radius of the circle
		circle_radius = float(input('Enter the radius of the circle: '))
			
		#finds the circumference
		circle_circumference = 2 * pi * circle_radius ** 2
		
		#prints the results
		print('Circumference = 2 * pi * radius')
		print('Circumference = 2 * pi *', circle_radius)
		print('Circumference =', circle_circumference)
		
	#asks the user to choose another operation or quit
	circle_go_again = str(input('Press y for another operation or n to quit: '))
	
	if circle_go_again == 'y':
		menu()
	else:
		sys.exit
	
	#end of circles
	return
#}}}

#triangle definition
#{{{ 
def func_triangles():
	#instructions to get started
	print('Select the number of the operation you want: ')
	
	#triangles menu
	print('1: Find Perimeter')
	print('2: Find Area')
	print('3: Find an Unknown Side')
	print('4: Find an Unknown Angle')
	
	#allows user to make their pick
	select_triangle_operation = int(input(">"))

	#if the user chose perimeter
	if select_triangle_operation == 1:
		#gets side 1 from the user
		triangle_side1 = float(input('Enter the length of side 1: '))
		
		#gets side 2 from the user
		triangle_side2 = float(input('Enter the length of side 2: '))
		
		#gets side 3 from the user
		triangle_side3 = float(input('Enter the length of side 3: '))

		#computes the perimeter
		triangle_perimeter = triangle_side1 + triangle_side2 + triangle_side3
		
		#prints the results
		print('Perimeter = side 1 + side 2 + side 3')
		print('Perimeter =', triangle_side1, '+', triangle_side2, '+', triangle_side3)
		print('Perimeter = ', triangle_perimeter)
		
		triangle_go_again = str(input('Press y for another operation, n to quit: '))
		
		#checks to see what the user chose
		if triangle_go_again == 'y':
			#returns to the main menu
			menu()
		else:
			#quits the program
			sys.exit()
		
	#if the user chose area
	elif select_triangle_operation == 2:
		#gets the base from the user
		triangle_base = float(input('Enter the base of the triangle: '))
		
		#gets the height from the user
		triangle_height = float(input('Enter the height of the triangle: '))
		
		#the calculation
		triangle_area = 0.5 * triangle_base * triangle_height
		
		#prints the results
		print('Area = 0.5 * b * h')
		print('Area = 0.5 *', triangle_base, '*', triangle_height)
		print('Area =', triangle_area)
		
		triangle_go_again = str(input('Press y for another operation, n to quit: '))
		
		#checks to see what the user chose
		if triangle_go_again == 'y':
			#returns to the main menu
			menu()
		else:
			#quits the program
			sys.exit()
		
	#if the user chose unknown side	
	elif select_triangle_operation == 3:
		#gets side 1 from the user
		triangle_side1 = float(input('Enter the length of side 1: '))
		
		#gets side 2 from the user
		triangle_side2 = float(input('Enter the length of side 2: '))
		
		#gets the perimeter from the user
		triangle_perimeter = float(input('Enter the perimeter of the triangle: '))
		
		#computes the third side
		triangle_side3 = triangle_perimeter - (triangle_side1 + triangle_side2)
			
		#prints the results
		print('Side 3 = Perimeter - (Side 1 + Side 2)')
		print('Side 3 =', triangle_perimeter, '-', (triangle_side1 + triangle_side2))
		print('Side 3 =', triangle_side3)
		
		triangle_go_again = str(input('Press y for another operation, n to quit: '))
		
		#checks to see what the user chose
		if triangle_go_again == 'y':
			#returns to the main menu
			menu()
		else:
			#quits the program
			sys.exit()
			
	#if the user chose unknown angle
	if select_triangle_operation == 4:
		#gets the 1st angle from the user
		triangle_angle1 = float(input('Enter angle 1: '))
		
		#gets the 2nd angle from the user
		triangle_angle2 = float(input('Enter angle 2: '))
		
		#calculates the sum of the known angles
		triangle_known_angles = triangle_angle1 + triangle_angle2
		
		#finds the third angle
		triangle_unknown_angle = 180 - triangle_known_angles
		
		#prints the result
		print('Unknown angle = 180 -(angle 1 + angle 2)')
		print('Unknown angle = 180 - (', triangle_angle1, '+', triangle_angle2, ')')
		print('Unknown angle =', triangle_unknown_angle)
		
	triangle_go_again = str(input('Press y for another operation, n to quit: '))
		
	#checks to see what the user chose
	if triangle_go_again == 'y':
		#returns to the main menu
		menu()
	else:
		#quits the program
		sys.exit()
		
	#end of triangles
	return
#}}}

#rectangle definition
#{{{ 
def func_rectangle():
	#lets the user choose perimeter or area
	print("Select the number of the operation you wish to perform:")
	print('1: Find perimeter')
	print('2: Find area')
	
	select_rectangle_operation = int(input(">"))
	
	if select_rectangle_operation == 1:
		#gets the length
		rectangle_length = float(input("Enter the length of the rectangle: "))
	
		#gets the width
		rectangle_width = float(input("Enter the width of the rectangle: "))
		
		#calculates the perimeter
		rectangle_perimeter = (2 * rectangle_length) + (2 * rectangle_width)
		
		#prints the results on screen
		print('Perimeter = 2L * 2W')
		print('Perimeter = (2 * length) + (2 * width)')	
		print('Perimeter =', rectangle_perimeter)
		
	elif select_rectangle_operation == 2:
		#gets the length
		rectangle_length = float(input("Enter the length of the rectangle: "))
	
		#gets the width
		rectangle_width = float(input("Enter the width of the rectangle: "))
		
		#computes the area
		rectangle_area = rectangle_length * rectangle_width
		
		#prints the results
		print('Area = length * width')
		print('Area =', rectangle_length, '*', rectangle_width)
		print('Area =', rectangle_area)
		
	#asks the user if they want to make another calculation
	rectangle_go_again = str(input("Press y for another operation or n to quit: "))
	
	#checks what the user chose
	
	#if the user chose another operation
	if rectangle_go_again == 'y':
		#call to menu
		menu()
		
	#if the user chose to quit
	else:
		sys.exit()
		
	#if the user chose area
	if select_rectangle_operation == 2:
		#gets the length
		rectangle_length = float(input("Enter the length of the rectangle: "))	

		#gets the width
		rectangle_width = float(input("Enter the width of the rectangle: "))

		#the calculation
		rectangle_area = rectangle_length * rectangle_width	

		#prints the area on screen
		print("The area of a rectangle whose length is", rectangle_length, "and width is", rectangle_width, rectangle_area)
		
	#asks the user if they want to make another calculation
	rectangle_go_again = str(input("Press y for another operation or n to quit: "))
	
	#checks what the user chose
	
	#if the user chose another operation
	if rectangle_go_again == 'y':
		#call to menu
		menu()
		
	#if the user chose to quit
	else:
		sys.exit()
		
	#end of rectangle
	return
#}}}

#squares definition
#{{{ 
def func_squares():
	#intro message
	print('Press the number associated with the operation below:')
	print('1: Find perimeter')
	print('2: Find area')
	
	#allows user to choose the operation
	select_square_operation = int(input(">"))
	
	#tests which operation the user chose
	
	#if the user chose perimeter
	if select_square_operation == 1:
		#gets the length of the side from the user
		square_side = float(input("Enter the length of the side: "))
		
		#calculates the perimeter
		square_perimeter = square_side * 4
		
		#prints the results
		print('Perimeter = s * 4')
		print('Perimeter =', square_side, '* 4')
		print('Perimeter = ', square_perimeter)
	
	#if the user chose area
	elif select_square_operation == 2:
		#gets the length of the side from the user
		square_side = float(input("Enter the length of the side: "))
		
		#calculates the area
		square_area = square_side ** 2
				
		#prints the results
		print('Area = s ** 2')
		print('Area =', square_side, '** 2')
		print('Area =', square_area)
	
	#asks the user if they want to make another calculation
	squares_go_again = str(input("Press y for another operation or n to quit: "))
	
	#checks what the user chose
	
	#if the user chose another operation
	if squares_go_again == 'y':
		#call to menu
		menu()
		
	#if the user chose to quit
	else:
		sys.exit()
		
	#end of squares
	return #}}}

#menu definition
#{{{ 
def menu():
	#instructions to pick the shape
	print("Press the number associated with the shape you want to work with to get started:")

	#to select squares
	print("1: Squares")
	
	#to select rectangles
	print("2: Rectangles")
	
	#to select triangles
	print("3: Triangles")
	
	#to select circles
	print("4: Circles")
	
	#variable to choose shape
	select_shape = int(input(">"))
	
	#checks which shape the user chose
	
	#if the user chose squares
	if select_shape == 1:
		#call to squares function
		func_squares()
	
	#if the user chose rectangles
	elif select_shape == 2:
		#call to rectangle function
		func_rectangle()
	
	#if the user chose triangles
	elif select_shape == 3:
		func_triangles()
		
	#if the user chose circles
	elif select_shape == 4:
		func_circles()
		
	#end of menu
# 	return
	
#}}}

#main definition
#{{{ 
def main():
	#lets the user choose to start the program or quit it
	begin_or_quit = str(input("Press b to begin or q to quit: "))
	
	#tests to see what the user chose
	
	#if the user chose to begin
	if begin_or_quit == 'b':
		#calls the main menu if the user chose to begin
		menu()
		
	#if the user chose to quit
	else:
		#call to sys.exit to quit
		sys.exit()
#end main
#}}}

#function calls

#call to main
main()
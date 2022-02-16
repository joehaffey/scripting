'''
file name multiples.py
created by joe haffey on monday december 27, 2021 at 7:28 pm
this program finds multiples of a number to an upper bound specified by the user.  it asks the user to pick the start number and the upperbound.  then it calculates the multiples of the start number using a for loop.  
'''

#main definition
def main():
	#for the starting number	
	global start_number
	
	#gets the start number
	start_number = int(input('enter the start number: '))
	
	#for the upper limit
	global upper_bound
	
	#gets the upper bound
	upper_bound = int(input('enter the upper limit: '))
	
	#end of main
	return start_number, upper_bound

#calculates the multiples
def calculate(start_number, upper_bound):
	#for the loop counter
	ctr = int(0)

	#variable for the multiples
	multiple = start_number
	
	#prints the results
	print("the multiples of ", start_number, "up to", upper_bound, "are: \n")
	
	#this loop checks all numbers between start_number and upper_bound
	for ctr in range(start_number, upper_bound):
		#checks to see if the counter is divisible by start_number
		if ctr % start_number == 0:
			print(ctr)
			
		#increments the counter
		ctr = ctr + 1
		
	#end of calculate
	return
	
#call to main
main()

#call to calculate
calculate(start_number, upper_bound)
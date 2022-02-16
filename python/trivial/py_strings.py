'''
file name py_strings.py
created by joehaffey on tuesday december 28, 2021 at 7:24 pm
this program demonstrates passing of strings to functions in python.  it asks the user to enter an initial string.  then it asks for three more strings. then the initial string in concatenated to the other 3 strings.
'''

#main definition
def main():
	#for the initial string
	global initial_string
	
	#gets the initial string from the user
	initial_string = str(input('enter a word of any length: '))

#get_string definition
def get_strings():
	#for the list
	global words 
	
	#gets list populated
	words = []
	
	#for the number of strings inputted
	stop_value = int(0)
	#gets stop_value from user
	stop_value = int(input('enter the number of strings you need: '))
	
	#counter for the loop
	ctr = int(0)
	
	#loop to get the strings
	for ctr in range(0, stop_value):
		#gets the list elements from the user
		element = str(input('enter a word of any length: '))
		
		#increments the counter
		ctr = ctr + 1
		
#combine definition
def combine(initial_string, words):
	for element in range(words):
		print(initial_string + words)
		
	return 
			
#call to main
main()

#call to get_strings
get_strings()

#call to combine
combine()
import sys

#module simple.py
print('module simple loaded')

def func1():
	print('func1 called')
	
def func2():
	print('func2 called')
	
	
stop_or_go = int(input('press 1 to continue, 2 to quit: '))
if stop_or_go == 1:
	func1()
	func2()
else:
	print('quitting program')
	sys.exit()

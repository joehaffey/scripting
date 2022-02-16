#file name temperature.py
#created by joehaffey on saturday october 2, 2021 at 11:56 am
#this file demonstrates the if block in python by converting temperatures from one temperature scale to another.  for now, it is just fahrenheit and celcius.

#gets the temperature from the user
temp = float(input('Enter the temperature: '))
scale = str(input('Enter the scale f for fahrenheit or c for celcius: '))

#this if block performs the calculations else is performed if the user picks c for the scale
if scale == 'f':
	converted_temp = (temp - 32) * 0.5556
	print(temp, 'converted to celcius is ', converted_temp)
else:
	converted_temp = (temp * 1.8) + 32
	print(temp, 'converted to fahrenheit is ', converted_temp)
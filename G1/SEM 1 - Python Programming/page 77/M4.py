# Temperature Conversion Program  (Celsius to Fahrenheit)
# This program will convert a temperature entered in Celsius
# to the equivalent degrees in Fahrenheit

# program greeting 
print('This program will convert degrees Celsius to degrees Fahrenheit') 

# get temperature in Fahrenheit 
celsius = float(input('Enter degrees Celsius: ')) 

# calc degrees Celsius 
fahren = ( celsius * 9/5 )- 32

# output degrees Celsius 
print(celsius, 'degrees Celsius equals', format(fahren, '.1f'), 'degrees Fahrenheit') 
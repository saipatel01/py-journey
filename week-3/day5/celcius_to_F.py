#convert celcius to fahrenheit
def celcius_to_fahrenheit(x):
    fahrenheit =( x * 9/5) +32
    return fahrenheit


sai =int(input("Enter celcius degress:"))
converted_celcius=celcius_to_fahrenheit(sai)
print("converted temp:",converted_celcius)
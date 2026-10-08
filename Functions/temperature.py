def temperature(temp, unit):
    if unit == 'C':
        return temp *9/5 + 32 ##Celsius To fahrenheit
    elif unit == 'F':
        return (temp-32)*5/9 ##Fahrenheit to Celsius
    else:
        return temp

print(temperature(25, 'C'))
print(temperature(77, 'F'))
print(temperature(77, 'E'))
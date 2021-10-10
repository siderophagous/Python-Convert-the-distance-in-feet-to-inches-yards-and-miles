# Python Program for simple Unit Converter

num1 = input('Enter the value: ')
unit1 = input('Which unit do you want it converted from:  ')
unit2 = input('Which unit do you want it converted to: ')

if unit1 == "cm" and unit2 == "m":
    ans = float(num1)/100
    print(ans)
elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1)/10
    print(ans)
elif unit1 == "m" and unit2 == "cm":
    ans = float(num1)*100
    print(ans)
elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1)*10
    print(ans)
elif unit1 == "mm" and unit2 == "m":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "m" and unit2 == "mm":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "km" and unit2 == "m":
    ans = float(num1)*1000
    print(ans)
elif unit1 == "m" and unit2 == "km":
    ans = float(num1)/1000
    print(ans)
elif unit1 == "mm" and unit2 == "km":
    ans = float(num1)/1000000
    print(ans)
elif unit1 == "ft" and unit2 == "cm":
    ans = float(num1)*30.48
    print(ans)
elif unit1 == "ft" and unit2 == "mm":
    ans = float(num1)*304.8
    print(ans)
elif unit1 == "ft" and unit2 == "inch":
    ans = float(num1)*12
    print(ans)
elif unit1 == "inch" and unit2 == "cm":
    ans = float(num1)*2.54
elif unit1 == "inch" and unit2 == "mm":
    ans = float(num1)*25.4

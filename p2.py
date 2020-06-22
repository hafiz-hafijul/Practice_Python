weight = float( input('Weight : '))
c = weight/.45
k = weight*.45


unit = input('Press kilo(k) or pounds (l) : ')


if unit =="k" :
    print('Your weight in : ' , k ,'kilograms')
else:
    print('Your weight in : ' , c , 'Pounds')

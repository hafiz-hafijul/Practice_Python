phone = input('Phone : ')

dic1 = {
    '0' : 'zero ',
    '1' : 'one ',
    '2' : 'two ',
    '3' : 'three ',
    '4' : 'four ',

}
output = ''
for ch in phone:
    output += dic1.get(ch , '!') + ''
print(output)
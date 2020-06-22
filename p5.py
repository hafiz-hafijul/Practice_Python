
while True :
    unit = input('> ').lower()


    if unit=='start':
        print('Car Started ....Ready to go.')
    elif unit == 'stop':
        print('Car Stopped')
    elif unit == 'quite':
        print()
        break
    else:
        print('I don\'t understand that ...')
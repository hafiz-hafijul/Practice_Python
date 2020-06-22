screat_number = 10
loops_limit = 3
guess_number = 0

while guess_number < loops_limit:
    guess = int(input('Guess : '))
    guess_number = guess_number + 1
    if screat_number == guess:
        print('WOW, You won!')
        break
else:
    print('Sorry,You Failed!')

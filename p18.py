main_password = 101875
main_email = "abc@gmail.com"
test_time = 3
start_time = 0

while start_time < test_time:

    def log(start_time=True):
        mail = input('Enter your email : ')
        if main_email == mail:
            password = int(input('Enter your password : '))
            start_time += 1
            if main_password == password:
                pass
            start_time += 102222
        else:
            print('Your email is incorrect. ')
        return f'ok'
logging = log()
print(logging)

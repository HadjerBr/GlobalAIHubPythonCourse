logInInformation = {'username1': 'password1', 'username2': 'password2', 'username3': 'password3'}
name = input('Enter username: ')
if name in logInInformation.keys():
    password = input('Enter password: ')
    if str(logInInformation[name]) == password:
        print('Welcome', name)
    else:
        print('Invalid password')

else:
    print('Invalid user name')
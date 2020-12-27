def get_info_string(name = None, lastname = None, date = None, city = None, email = None, phone_number = None):
    return f'{name} {lastname}, дата рождения {date}, город {city}, e-mail: {email}, тел: {phone_number}'


while True:
    try:
        name, l_name = input('Enter name and last name: ').split()
        break
    except ValueError:
        print('You should enter your name and last name with space between them. Try again!')
date_of_birth = input('Enter your date of birth: ')
city = input('Enter your city: ')

print(get_info_string(name=name, lastname=l_name, city=city, date=date_of_birth))

while True:
    try:
        name, l_name = input('Enter name and last name: ').split()
        break
    except ValueError:
        print('You should enter your name and last name with space between them. Try again!')
date_of_birth = input('Enter your date of birth: ')
city = input('Enter your city: ')
email = input('Enter your E-mail: ')
ph_number = input('Enter your phone number: ')

print(get_info_string(name=name, lastname=l_name, city=city, date=date_of_birth, phone_number=ph_number, email=email))


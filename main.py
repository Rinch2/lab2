password = input("Введите пароль: ")
password2 = input("введите пароль еще раз: ")

if password == password2:
    if len(password) > 6 and password.islower():
        print("Пароль принят")
    elif len(password) > 6 and password.isupper():
        print("Пароль принят")
    elif len(password) > 6 and password.isnumeric():
        print("Пароль принят")
    elif len(password) > 6 and password.isdigit():
        print("Пароль принят")
    elif len(password) > 6 and password.isalpha():
        print("Пароль принят")
    else:
        print("Пароль не принят")
else:
    print("Введён неправильный пароль")
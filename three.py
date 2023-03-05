year = input("Введите год: ")

a = int(year)

if a % 4 == 0 and (a % 100 != 0 or a % 400):
    b = str(a)
    print("Год " + b + " високосный")
else:
    b = str(a)
    print(b + " Не високосный год")
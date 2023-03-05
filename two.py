place = input("Введите ваше место: ")

if place.isalpha():
    print("Введите число")
else:
    a = int(place)
    if a <= 36 and a % 2 == 0:
        print("Ваше место в купе сверху")
    elif a <= 36 and a % 2 == 1:
        print("Ваше место в купе снизу")
    elif a <= 54 and a % 2 == 0:
        print("Ваше место боковое сверху")
    elif a <= 54 and a % 2 == 1:
        print("Ваше место боковое снизу")
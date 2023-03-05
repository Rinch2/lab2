colors = {"red": 1, "blue": 2, "yellow": 4}
all = {1: "red", 2: "blue", 3: "purple", 4: "yellow", 5: "orange", 6: "green"}

color = input("Введите первый цвет: ")
color2 = input("Введите второй цвет: ")

if color not in colors.keys() or color2 not in colors:
    print("Ошибка")

itog = colors[color] | colors[color2]
ok = all[itog]
print(ok)
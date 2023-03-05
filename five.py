list1 = []
N = input("Введите кол-во слов которые хотите соединить: ")
ch = int(N)

for _ in range(ch):
    list1 += list(map(str, input("Слово: ").split()))

end = ""
for word in list1:
    end = end + " " + word
print(end)

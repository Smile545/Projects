import modules

word = modules.random_choice()
li = list(word)
slovo = ["_"] * len(word)
win = False
i = 0

picture = ["_______   ",
           "|      |  ",
           "|      o  ",
           "|    / | \ ",
           '|      |   ',
           "|     /  \ ",]
while win != True:
    check = input("Введите букву: ")
    if check in li: 
        x = word.find(check)
        slovo[x] = check
        li[x] = ("_")
        print(slovo)
        if "_" not in slovo:
            s = "".join(slovo)
            print(f"Вы победили, итоговое слово {s}")
            win = True
    else:
        i += 1
        print("\n".join(picture[:i]))
        if i == 6:
            print("Ты проиграл((")
            break

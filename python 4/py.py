
# sorted tartiblash

# name = input("ismingizni kiriting: ")
# name2 = input("ismingizni kiriting: ")
# name3 = input("ismingizni kiriting: ")
# name4 = input("ismingizni kiriting: ")
# name5 = input("ismingizni kiriting: ")
# name6 = input("ismingizni kiriting: ")
# name7 = input("ismingizni kiriting: ")
# name8 = input("ismingizni kiriting: ")
# name9 = input("ismingizni kiriting: ")
# name10 = input("ismingizni kiriting: ")

# result = [name, name2, name3, name4, name5, name6, name7, name8, name9, name10]
# print(sorted(result))



# num = int(input('sonni kiriting: '))
# num2 = int(input('ikkichi sonni kiriting: '))
# resul1 = input('Amalni kiriting: ')

# if resul1 == '+':
#     print("Natija: " + str(num + num2))
# elif resul1 == '-':
#     print("Natija: " + str(num - num2))
# elif resul1 == '*':
#     print("Natija: " + str(num * num2))
# elif resul1 == '/':
#     print("Natija: " + str(num / num2))
    

# num3 = int(input('sonni kiriting: '))
# num4 = int(input('ikkichi sonni kiriting: '))
# resul2 = input('Amalni kiriting: ')

# if resul2 == '+':
#     print("Natija: " + str(num3 + num4))
# elif resul2 == '-':
#     print("Natija: " + str(num3 - num4))
# elif resul2 == '*':
#     print("Natija: " + str(num3 * num4))
# elif resul2 == '/':
#     print("Natija: " + str(num3 / num4))


# try:
#     name = 'javohir'
#     name2 = 35
#     print(name/name2)
# except NameError:
#     print('string va numberni bo`lib bo`lmaydi!!!')


try:
    file = open('file.html', 'r')
    start = file.read()
    print(start)
except FileNotFoundError:
    file = open('file.html', 'w')
    start = file.write("<h1>Afsuski siz izlagan file yo'q</h1>")
import math

clovar = {'Колесо': 'резина',
          'Масло': 'секрет', 'Диски': 'сталь'}
clovarr = {'Колесо': 10, 'Масло': 5, 'Диски': 50}
clovarrr = {'Колесо': 10, 'Масло': 5, 'Диски': 10}
choice = 50
list = ['Колесо', 'Масло', 'Диски']
print('1.	Просмотр описания: название – описание.')
print('2.	Просмотр цены: название – цена.')
print('3.	Просмотр количества: название – количество.')
print('4.	Всю информацию.')
print('5.	Покупка')
print('6.  Вызов меню.')
print('7.	До свидания')
while (choice != 7):
    choice = int(input('Ваш выбор: '))
    if choice == 6:
        print('1.	Просмотр описания: название – описание.')
        print('2.	Просмотр цены: название – цена.')
        print('3.	Просмотр количества: название – количество.')
        print('4.	Всю информацию.')
        print('5.	Покупка')
        print('6.  Вызов меню.')
        print('7.	До свидания')
    if choice == 4:
        for i in range(3):
            str = list[i]
            print()
            print(str, 'Материал', 'Цена', 'Кол-во')
            print('     ', clovar[str], '  ', clovarr[str], ' ', clovarrr[str])
            print()
    if choice == 1:
        str = input('Введите название товара: ')
        l=0
        for i in range (3):
          if str==list[i]:
            l=1
        if l==0:
            print('Такого товара нет')
        else:
          print('Состав: ', clovar[str])

    if choice == 2:
        str = input('Введите название товара: ')
        print('Цена: ', clovarr[str])
    if choice == 3:
        str = input('Введите название товара: ')
        print('Кол-во: ', clovarrr[str])
    if choice == 5:
        str = input('Введите название товара: ')
        print('На складе есть: ', clovarrr[str])
        k = int(input('Введите кол-во: '))
        if k > clovarrr[str]:
            print('На складе недостаточно товара')
            print('Желаете продолжить покупку?')
            print('1. Да')
            print('2. Нет')
            choice2 = int(input())
            if choice2 == 1:
                print('На складе есть: ', clovarrr[str])
                k = int(input('Введите кол-во: '))
                while (k > clovarrr[str]):
                    print('На складе есть: ', clovarrr[str])
                    k = int(input('Введите правильное кол-во: '))
                sum = 0
                sum = sum + k * clovarr[str]
                print('Стоимость:', sum)
                print('Спасибо за покупку!')
                clovarrr[str] = clovarrr[str] - k
        else:
            sum = 0
            sum = sum + k * clovarr[str]
            print('Стоимость:', sum)
            print('Спасибо за покупку!')
            clovarrr[str] = clovarrr[str] - k

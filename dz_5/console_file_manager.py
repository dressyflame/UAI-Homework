



import os, sys, shutil
from pathlib import Path

import victory, account

actionlist = ['1 - создать папку',
              '2 - удалить (файл/папку)',
              '3 - копировать (файл/папку)',
              '4 - просмотр содержимого рабочей директории',
              '5 - посмотреть только папки',
              '6 - посмотреть только файлы',
              '7 - просмотр информации об операционной системе',
              '8 - создатель программы',
              '9 - играть в викторину',
              '10 - мой банковский счет',
              '11 - смена рабочей директории (*необязательный пункт)',
              '12 - выход']
while (1):
    print(*actionlist, sep = '\n')
    n = int(input("Выберите действие: "))
    if (n == 1):
        name = input('Введите имя папки: ').strip()
        if name in os.listdir():
            print('Папка с таким именем уже существует!')
        else:
            os.mkdir(name)
            print('Папка '+name+' создана в текущей директории!' )
    elif (n == 2):
        name = input('Введите имя папки или файла: ').strip()
        if name not in os.listdir():
            print('Папки или файла с таким именем не существует!')
        else:
            my_file = Path('./'+name)
            if my_file.is_file():
                os.remove(name)
                print('Файл '+name+' удален из текущей директории!' )
            else:
                os.rmdir(name)
                print('Папка '+name+' удалена из текущей директории!' )
            
    elif (n == 3):
        name = input('Введите имя папки или файла: ').strip()
        if name not in os.listdir():
            print('Папки или файла с таким именем не существует!')
        else:
            dst = input('Введите путь копирования: ').strip()
            if dst in os.listdir():
                print('В рабочей директории уже существует файл с таким именем')
            else:
                shutil.copy(name, dst)
    elif (n == 4):
        print('Содержимое рабочей директории:')
        print(*os.listdir(), sep = '\n')
    elif (n == 5):
        print('Папки рабочей директории:')
        for i in os.listdir():
            my_file = Path('./'+i)
            if not my_file.is_file():
                print(i)
    elif (n == 6):
        print('Файлы рабочей директории:')
        for i in os.listdir():
            my_file = Path('./'+i)
            if my_file.is_file():
                print(i)
        
    elif (n == 7):
        print('Вы работаете в операционной системе: ' + sys.platform)
    
    elif (n == 8):
        print('Создатель программы - Коданев Никита')
    
    elif (n == 9):
        print()
        victory.victory()
        
    elif (n == 10):
        print()
        account.count()
            
    #elif (n == 11):
                
    elif (n == 12):
        print("Досвидания!")
        break                
    else:
        print('Нет такого действия!')
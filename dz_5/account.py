"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""


def print_history(history):
    if len(history) == 0:
        s = 'Вы еще не совершили ни одной покупки.'
    else:
        s = 'название - сумма'
        for i in range(len(history)):
            s += ('\n' + str(history[i][0]) + ' - ' + history[i][1])
    return s


def purchase(name, cost, account):
    #Добавлен тернарный оператор
    return "Это слишком дорого, у вас недостаточно средств!" if cost > account else (cost, (name, str(cost)))
        

def count():
    #exceptions
    try:
        with open('deposit.txt', 'r') as f:
            account = int(f.read())
    except:
        account = 0
    try:
        with open('purchase_history.txt', 'r') as f:
            #добавлен генератор списка
            history = [tuple(x.split(' - ')) for x in f.read().strip().split('\n')]
    except:
        history = []
    while True:
        print(f'На вашем счёте {account} средств, и {len(history)} покупок')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
    
        choice = input('Выберите пункт меню: ')
        if choice == '1':
            deposit = int(input('Введите сумму пополнения счета: '))
            account += deposit
        elif choice == '2':
            cost = int(input("Введите стоимость покупки: "))
            name = input("Введите название покупки: ").strip()
            pur = purchase(name, cost, account)
            if type(pur) != str:
                account -= pur[0]
                history.append(pur[1])
            else:
                print(pur)
        elif choice == '3':
            print(print_history(history))
        elif choice == '4':
            with open('deposit.txt', 'w') as f:
                f.write(str(account))
            with open('purchase_history.txt', 'w') as f:
                for i in history:
                    f.write(i[0] + ' - ' + i[1] + '\n')
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    count()
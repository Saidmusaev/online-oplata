login = str("user")
password = str("1234")

print("1.Вход \n2.Регистрация")
reg = input("Выберите ")
if reg == "1":
    login_input = str(input("Введите свой логин "))
    password_input = str(input("Введите свой пароль "))
    while login.upper == login_input.upper and password_input == password:
        print("1.Баланс")
        print("2.Переводы в другую карту")
        print("3.Оплата сим-карты")
    else:
        print("Неправильный логин или пароль")
elif reg == "2":
    reg_login = str(input("Создайте логин"))
    reg_pass = str(input("Создайте пароль"))
    print("1.Баланс")
    print("2.Переводы в другую карту")
    print("3.Оплата сим-карты")
else:
    print("Введите цифру 1 или 2")

class Payme:
    def __init__(self, balance, perevod, paynet):
        self.balance = balance
        self.perevod = perevod
        self.paynet = paynet

karta = Payme(100000, "Введите номер карты ", "Введите номер сим-карты ")

menu=int(input("Выберите операцию: "))
if menu == 1:
    print(karta.balance)
elif menu == 2:
    print(karta.perevod)
    nomer=input("")
    if len(nomer)==16:
        s = int(input("Введите сумму"))
        if s <= karta.balance:
            print("Успешно переведено")
        else:
            print("Не хватает средств")
    else:
        print("Введите 16 цифр в карте")
elif menu == 3:
    simkarta=int(input(print(karta.paynet)))
    summa=int(input("Введите сумму "))
    if summa<=karta.balance:
        print("Успешно переведено")
    else:
        print("Нехватает средств")
else:
    print("Нету такой операции")


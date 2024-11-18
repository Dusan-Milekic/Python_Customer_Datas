from colorama import Fore
class Customer:
    def __init__(user,id,name,lastname,address,job,money):
        user.id = id
        user.name = name
        user.lastname = lastname
        user.address = address
        user.job = job
        user.money = money

    def ShowFullName(user):
        print(f"My name is {user.name} {user.lastname}")

    def ShowMoney(user):
        print(f"Right now, I have {user.money} rsd.")



#Print all datas about customers
def PaintRowsCustomers(datas: list[Customer]):
    iterator: int = 0
    for x in datas:
        if iterator % 2 == 0:
            print(Fore.LIGHTBLUE_EX, x)
        else:
            print(Fore.LIGHTRED_EX, x)
        iterator += 1
    print(Fore.LIGHTWHITE_EX)




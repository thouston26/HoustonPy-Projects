#Creating Person Class

class Person:
    def __init__(self, name, address, tel_num):
        self.__name = name
        self.__address = address
        self.__tel_num = tel_num

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_tel_num(self, tel_num):
        self.__tel_num = tel_num

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel_num(self):
        return self.__tel_num




#Creating Customer Class
class Customer(Person):
    def __init__(self, name, address, tel_num, cus_num=0, mail=True or False):
        Person.__init__(self, name, address, tel_num)
        self.__cus_num = cus_num
        self.__mail = mail

    def set_cus_num(self, cus_num):
        self.__cus_num = cus_num

    def set_mail(self, mail):
        self.__mail = mail


    def get_cus_num(self):
        return self.__cus_num

    def get_mail(self):
        return self.__mail

#Main loop
def main():
    n = eval(input('Enter number of customers: '))
    lst = []
    for x in range(n):
        name = input("Enter name: ")
        address = input("Enter address: ")
        cusNum = int(input("Enter customer number: "))
        telNum = input("Enter telephone number: ")
        mail = bool(input("Enter mail id: "))
        c = Customer(name, address, telNum, cusNum, mail)
        lst.append(c)

    for x in range(n):
        print(lst[x].get_name(), lst[x].get_address(), lst[x].get_tel_num(), lst[x].get_cus_num(), lst[x].get_mail())

main()
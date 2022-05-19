#Employee class

class Employee():

    #Constructor of class

    def __init__(self,employee,empNumber):

        #Employee and empNumber accept here

        self.employee = employee

        self.empNumber = empNumber

#Inheritance happened here

class ProductionWorker(Employee):

    #Constructor of the ProoductionWorker class

    def __init__(self,employee,empNumber,shiftNumber,hourlyPay):

        #Employee class constructor

        Employee.__init__(self,employee,empNumber)

        #Accept the shiftNumber and hourlyPay

        self.shiftNumber = shiftNumber

        self.hourlyPay = hourlyPay

    #Display values

    def show(self,*args):

        print()

        print(" Employee Name =",self.employee)

        print()

        print(" Employee Number =",self.empNumber)

        print()

        print(" Employee shift Number =", self.shiftNumber)

        print()

        print(" Employee hourly pay rate =", self.hourlyPay)

        print()

    #___str__ method

    def __str__(self):

        print(self.shiftNumber,self.hourlyPay)

print()

employee = input("Enter employee name = ")

print()

empNumber = input("Enter employee Number = ")

print()

shiftNumber = input("Enter shiftNumber = ")

print()

hourlyPay = input("Enter hourly pay rate = ")

print()

#Object of the production worker class

productionObject = ProductionWorker(employee,empNumber,shiftNumber,hourlyPay)

#Method call through object

productionObject.show()

#__str__() method call through object

productionObject.__str__()
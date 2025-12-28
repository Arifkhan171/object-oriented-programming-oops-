#                       Static variable
# static varaible/ class variable is a varible that values are same for all object like serial no for each coustomer that only increase for each counter while instance variable is a vrarible that value are diffrent for all object
# static variable is always outside the class and instance variable is defined inside the class
# instane variable is written by self. while static varible is written by class name.  .





#
# class Atm:
#     counter=1
#     def __init__(self):   # def __init__(self):  is a spacial method called constructor that automatically call when the you make the object of that class
#      self.pin=""
#      self.balance=500001
#
#      self.sno=Atm.counter
#      Atm.counter=Atm.counter+1
#
#      # self.menue()
#
#     def menue(self):
#         user_input=input(""""
#          Hello , what you want
#          1. enter 1 to creat pin
#          2. enter 2 to deposit
#          3. enter 3 to withdraw
#          4. enter 4 to check the balance
#          5. enter 5 to exit
#         """)
#         if user_input=="1":
#             self.creat_pin()
#         elif user_input=="2":
#             self.Deposit()
#         elif user_input=="3":
#             self.withdraw()
#         elif user_input=="4":
#             self.check_balance()
#         else :
#             print("exit")
#
#     def creat_pin(self):
#         self.pin=input("enter you pin")
#         print("pin set successfuly")
#     def Deposit(self):
#         temp=input("enter your pin")
#         if temp==self.pin:
#             amount=int(input("enter your amount"))
#             self.balance=self.balance + amount
#             print("deposit successfuly")
#         else:
#             print('pin mismatch')
#     def withdraw(self):
#        temp=input("enter your pin")
#        if temp==self.pin:
#            amount=int(input("enter the amount you wabnt to withdraw"))
#            if amount <= self.balance:
#                self.balance=self.balance - amount
#                print(amount ,"withradaw succussefuly")
#            else:
#                print("your balance is less the amount  you want to withdraw")
#        else:
#            print("invilid pin")
#
#     def check_balance(self):
#         temp=input("enter your pin")
#         if temp==self.pin:
#             print("your balance is ",self.balance)
#         else:
#             print("invalid pin")
#
#
# obj1=Atm()
# obj2=Atm()
# obj3=Atm()
# print(obj1.sno)
# print(obj2.sno)
# print(obj3.sno)









class Atm:
    __counter=1
    def __init__(self):   # def __init__(self):  is a spacial method called constructor that automatically call when the you make the object of that class
     self.pin=""
     self.balance=500001

     self.sno=Atm.counter
     Atm.__counter=Atm.__counter+1

     # self.menue()
    @staticmethod
    def get_counter():
      return Atm.__counter
      print("jd")
    @staticmethod
    def set_counter(new):
     if type(new)==int:
          Atm.__counter=new

     else:
        print("invalid sno")
    def menue(self):
        user_input=input(""""
         Hello , what you want
         1. enter 1 to creat pin
         2. enter 2 to deposit
         3. enter 3 to withdraw
         4. enter 4 to check the balance 
         5. enter 5 to exit
        """)
        if user_input=="1":
            self.creat_pin()
        elif user_input=="2":
            self.Deposit()
        elif user_input=="3":
            self.withdraw()
        elif user_input=="4":
            self.check_balance()
        else :
            print("exit")

    def creat_pin(self):
        self.pin=input("enter you pin")
        print("pin set successfuly")
    def Deposit(self):
        temp=input("enter your pin")
        if temp==self.pin:
            amount=int(input("enter your amount"))
            self.balance=self.balance + amount
            print("deposit successfuly")
        else:
            print('pin mismatch')
    def withdraw(self):
       temp=input("enter your pin")
       if temp==self.pin:
           amount=int(input("enter the amount you wabnt to withdraw"))
           if amount <= self.balance:
               self.balance=self.balance - amount
               print(amount ,"withradaw succussefuly")
           else:
               print("your balance is less the amount  you want to withdraw")
       else:
           print("invilid pin")

    def check_balance(self):
        temp=input("enter your pin")
        if temp==self.pin:
            print("your balance is ",self.balance)
        else:
            print("invalid pin")



Atm.get_counter()
# Atm.set_counter(5)
# Atm.get_counter()

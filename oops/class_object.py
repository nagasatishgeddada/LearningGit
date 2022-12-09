class Car:  # creating Class
    attr1 = "Audi"
    attr2 = "Isuzu"  # def function_name for python

    def names(self):  # creating Function
        # self is used for retervieving
        print("The car name is :", self.attr1)
        print("The car name is :", self.attr2)  # writing convention


MyCar = Car()  # creating the objects  -MyCar is the object and car is class
print(MyCar.attr1)
MyCar.names()

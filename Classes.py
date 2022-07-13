class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attribute"""
        print("__init__ is running")
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")


# functions in class are called "method" and object are called "instance"
# the self parameter must be the first parameter in the all methods in a class
# self is the reference of the instance created
# variable that are accessed through instance are called attributes

my_dog = Dog('Stella', 3)

print(f"Dog name = {my_dog.name}")  # the attributes and method of the class are called using dot operator
print(f"Dog age = {my_dog.age}")

my_dog.sit()  # as it clearly visible that we are not passing any parameter for self
my_dog.roll_over()

# a class and consist of as many instances as required

my_dog2 = Dog('Johnny', 5)

print(f"Dog name = {my_dog2.name}")  # the attributes and method of the class are called using dot operator
print(f"Dog age = {my_dog2.age}")


class Car:
    """ Simple car class """

    def __init__(self, company, model, condition, price):
        self.model = model
        self.condition = condition
        self.company = company
        self.price = price
        print("parent")
        
    def get_discription(self):
        print(f"This car was created by company {self.company} in year {self.model} "
              f"also in {self.condition} condition and its price {self.price}")

    def update(self):

        update_var = input("Enter the company of the car")
        self.company = update_var
        update_var = input("Enter the model of the car")
        self.model = update_var  # + 2
        update_var = input("Enter the condition of the car")
        self.condition = update_var

    def price_increment(self, increment):
        self.price += increment

    def fill_gas_tank(self):
        print("Must regularly fill the gas")


my_car = Car('Toyota', 2019, 'Good', 2_000_000)

my_car.get_discription()
# my_car.update()
my_car.price = 2_550_000
my_car.price_increment(3_000)
my_car.get_discription()


class electricCars(Car):

    def __init__(self, company, model, condition, price):
        print('Child')
        super().__init__(company, model, condition, price)  # super() function helps to call to call a method from a
        #child class
        self.battery_size = 75


    def battery(self):
        print(f'The size of the battery is = {self.battery_size}')

    def fill_gas_tank(self):
        print('It runs on electricity')


my_electric_car = electricCars('Tesla', '2021', 'Excellent', 2_000_000)
my_electric_car.get_discription()
my_electric_car.battery()
my_electric_car.fill_gas_tank()

# in python the class atributes are always public
# python does not have private keyword but the encapsulation can be done by adding a underscore before that variable

# single inheritance


class Parent():
    def __init__(self):
        print("parent")
        super(Parent, self).__init__()
        print("Leaving parent")


class child(Parent):
    def __init__(self):
        print("child")  # the constructor of the parent class is not run automatically
        super().__init__()  # to run parent constructor write this code


my = child()

# multiple inheritance


class Parent2():
    def __init__(self):
        print("parent2")
        super(Parent2, self).__init__()
        print("Leaving parent2")


class chlid2(Parent, Parent2):
    def __init__(self):
        print("child2")
        super(chlid2, self).__init__()
        print("Leaving child2")

# another way to call constructor is an old method
# here we don't have to write a super() in parent class just explicitly call all that parent class constructor in child

# class chlid2(Parent, Parent2):
#     def __init__(self):
#         print("child2")
#         Parent.__init__(self)
#         Parent2.__init__(self)
#         print("Leaving child2")


print('Mutiple inheritance')
my2 = chlid2()

# multilevel inheritance



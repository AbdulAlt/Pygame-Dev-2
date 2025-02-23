# Defining a class to represent a family member
class Family:
    def __init__(self, fn, ln, age, relation):
        # Initializing family member attributes
        self.fn = fn
        self.ln = ln
        self.age = age
        self.relation = relation
    
    def full_name(self):
        # Returning the full name of the family member
        return self.fn + " " + self.ln

# Creating an instance of the Family class
father = Family("Father Mc.", "Fatherson", 36, "father")
print(father.full_name())

# Defining a class to represent a bank account
class Bank_account:
    def __init__(self, name, number, balance):
        # Initializing bank account attributes
        self.name = name
        self.number = number
        self.balance = balance

    def add_money(self):
        # Adding a fixed amount of money to the account balance
        money = 90000
        self.balance += money
    
    def display_account(self):
        # Displaying account details
        print("name: {}".format(self.name))
        print("number: {}".format(self.number))
        print("balance: {}".format(self.balance))

# Creating an instance of the Bank_account class
bank1 = Bank_account("Abdul", "008658", 0)
bank1.add_money()
bank1.display_account()

# Defining a class to represent a student
class Students:
    # Defining class variables with default values
    name = ""
    age = ""
    grade = ""
    school = "duck cool community school"
    class_teacher = "Mr. James"

    # Method to update student details
    def change_details(self):
        global name, age, grade
        # Getting user input for student details
        name = input("What is your name?\n")
        age = input("What is your age?\n")
        grade = input("What is your grade?\n")
    
    # Method to display student details
    def show_details(self):
        global school
        global class_teacher
        # Printing student details
        print("name: {}".format(name))
        print("age: {}".format(age))
        print("grade: {}".format(grade))
        print("school: {}".format(self.school))
        print("class teacher: {}".format(self.class_teacher))

# Creating an instance of the Students class
student1 = Students()
student1.change_details()
student1.show_details()

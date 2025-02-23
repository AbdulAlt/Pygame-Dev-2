class Family:
    def __init__(self, fn, ln, age, relation):
        self.fn = fn
        self.ln = ln
        self.age = age
        self.relation = relation
    
    def full_name(self):
        return self.fn + " " + self.ln

father = Family("Father Mc.", "Fatherson", 36, "father")
print(father.full_name())

# bank
class Bank_account:
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def add_money(self):
        money = 90000
        self.balance += money
    
    def display_account(self):
        print("name: {}".format(self.name))
        print("number: {}".format(self.number))
        print("balance: {}".format(self.balance))

bank1 = Bank_account("Abdul", "008658", 0)
bank1.add_money()
bank1.display_account()

# students class
class Students:
    # blank class variables
    name = ""
    age = ""
    grade = ""
    school = "duck cool community school"
    class_teacher = "Mr. James"

    # change details function
    def change_details(self):
        global name, age, grade
        name = input("What is your name?\n")
        age = input("What is your age?\n")
        grade = input("What is your grade?\n")
    
    # show details function
    def show_details(self):
        global school
        global class_teacher
        print("name: {}".format(name))
        print("age: {}".format(age))
        print("grade: {}".format(grade))
        print("school: {}".format(self.school))
        print("class teacher: {}".format(self.class_teacher))

student1 = Students()
student1.change_details()
student1.show_details()
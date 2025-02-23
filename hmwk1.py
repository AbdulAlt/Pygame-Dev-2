class You:
    name = ""
    age = ""
    description = ""
    def who_are_you(self):
        global name, age, description
        name = input("What is your name?\n")
        age = input("What is your age?\n")
        description = input("Describe yourself!\n")
        print("name: {}".format(name))
        print("age: {}".format(age))
        print("description: {}".format(description))

you = You()
print("\n")
you.who_are_you()

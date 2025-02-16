# libraries
import random

# Bird class
class Bird:
    no_of_teeth = 0
    no_of_legs = 2
    have_beak = True
    lay_eggs = True
    can_fly = True
    # lay eggs function
    def laying_eggs(self):
        return random.randint(1, 10)

# calling a variable using a class name
print(Bird.no_of_legs)
pigeon = Bird()
print(pigeon.can_fly)
chicken = Bird()
print(chicken.lay_eggs)
print(pigeon.laying_eggs())
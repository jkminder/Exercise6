from vehicle import *
import random

class Customer(object):
    
    def __init__(self,name):
        self._name = name
        self._score = self.credit_score()
    def __str__(self):
        return 'Customer: %s' % self.get_name()


    def credit_score(self):
        credit = random.randint(0,100)
        if credit > 60:
            return True
        else:
            return False

    def get_score(self):
        return self._score

    def get_name(self):
        return self._name


class VIP_Customer(Customer):

    def credit_score(self):
        return True


### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heidi

print(Wendy.get_score()) # expected output: True
print(Heidi.get_score()) # expected output: True

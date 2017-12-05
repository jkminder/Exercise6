from vehicle import *
from customer import *

class Employee(object):
    emp_id = 0

    def __init__(self, name):
        self._name = name
        self._id = Employee.emp_id
        Employee.emp_id += 1

    def __str__(self):
        return 'Employee: %s is of type %s' % (self._name, self.get_title())

    def get_name(self):
        return self._name
    
    def get_title(self):
        return 'Subordinate'
    
class Manager(Employee):

    def get_title(self):
        return 'Manager'

    def get_sales_report(self,salesman):
        assert isinstance(salesman, Salesman), 'salesman is not a Salesman Object'
        if salesman.get_name() not in Salesman.sales.keys():
            raise KeyError('This salesman does not have any sales yet')
        print('%s\'s current cumulative sales:\n%d'% (salesman.get_name(), Salesman.sales[salesman.get_name()]))


class Salesman(Employee):
    sales = {}

    def sale(self,vehicle,sales_price,customer):
        assert isinstance(vehicle, Vehicle), 'vehicle is not a Vehicle Object'
        assert isinstance(customer, Customer), 'customer is not a Customer Object'
        if customer.get_score():
            Salesman.sales[self.get_name()] = Salesman.sales.get(self.get_name(), 0) + sales_price
        else:
            print('Sorry the customer %s has not a high enough credit score' % customer.get_name())





### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric) # expected output: Employee: Eric is of type Manager
print(Kyle) # expected output: Employee: Kyle is of type Subordinate
print(Stan) # expected output: Employee: Stan is of type Subordinate
print(Kenny) # expected output: Employee: Kenny is of type Subordinate
print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

# Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000

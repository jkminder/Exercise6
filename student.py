from module import *
from moduleElement import *


class Student(object):
    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self, title):
        assert isinstance(title, Module), 'This is not a Module Object'
        self.modules.append(title)
        self.grades[title] = title.get_grade()

    def get_list_modules(self):
        print('Modules of %s:'% self.name)
        for i in self.modules:
            print('\t' + i.get_title())

    def get_grades(self):
        print('Grades of Student %s' % self.name)
        for key in self.grades:
            print('\t%s: %d' % (key.get_title(), self.grades[key]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6

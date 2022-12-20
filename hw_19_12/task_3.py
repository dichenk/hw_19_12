class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @fullname.setter
    def fullname(self, something):
        first, last = something.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = self.last = None


emp_1 = Employee('John', 'Smith')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print()

del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

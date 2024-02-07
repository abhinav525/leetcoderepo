class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __str__(self):
        return f"Name is {self.name}\n Salary is {self.salary}"
    
    def __eq__(self,other):
        return self.salary==other.salary
    
emp1=employee("kevin",450000)
print(emp1)
emp2=employee("richard",80000)
print(emp2)

print("-"*60)
#works for not equal also.if you are overloading eqaul to operator.
if (emp1==emp2):
    print(f"emp1 salary is equal to emp2 salary")
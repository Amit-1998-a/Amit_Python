class A:
    id=0
    name=""
    salary=0
    list1=[]

    def data(self, id, name, salary):
        self.id=id,
        self.name=name,
        self.salary=salary

    def set_id(self,id):
        self.id= id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

    def add(self, la):
        self.list1.append(la)

    def get(self):
        return self.list1


a=A()

for i in range (2):
    print("Enter the index number ",i)
    a.set_id(input("id :"))
    a.set_name(input("name:"))
    a.set_salary(input("salary :"))

    lst= {"id:", a.get_id() + " ", "name :", a.get_name(), "salary " , a.get_salary()}
    a.add(lst)
print(a.get())





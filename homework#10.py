

class Managers:
    def __init__(self, name, surname, age, department):
        self.name = name
        self.surname = surname
        self.age = age
        self.department = department

    def show_manager_info(self):
        print(f"Manager name: {self.name} {self.surname} Age: {self.age}")


class Employees:
    def __init__(self, name, surname, age, department):
        self.name = name
        self.surname = surname
        self.age = age
        self.department = department

    def show_employee_info(self):
        print(f"Eployee name: {self.name} {self.surname} Age: {self.age}")


class Company:
    def __init__(self, manager: list, employee: list):
        self.company_name = "Arcanum Software"    
        self.manager: list[Managers] = manager
        self.employee: list[Employees] = employee

    def workers(self):
        print(f"Number of people employed by the company: {len(self.manager) + len(self.employee)}")
        
        for managers in self.manager:
            managers.show_manager_info()
        
        for employees in self.employee:
            employees.show_employee_info() 

    def add_employee(self, new_employee: Employees):
        if isinstance(new_employee, Employees):
            self.employee.append(new_employee)
            return
        raise Exception(f"Provided value with incorrect type: {type(new_employee)}!")
    
    def add_manager(self, new_manager: Managers):
        if isinstance(new_manager, Managers):
            self.manager.append(new_manager)
            return
        raise Exception(f"Provided value with incorrect type: {type(new_manager)}!")

class Departments:
    # # departments = ["HR", "UX", "QA", "Software Engineering", "Product management"]
    # hr_departments = []
    # ux_departments = []
    # qa_departments = []
    # se_departments = []
    # pm_departments = []

    def __init__(self, managers: list, employees: list):
        self.managers: list[Managers] = managers
        self.employees: list[Employees] = employees
        self.departments = ["HR", "UX", "QA", "Software Engineering", "Product management"]
    
    def hr_workers(self):
        wk = []
        print(f"Workers of {self.departments[0]}: ")

        for i in range(len(self.managers)):
            if self.managers[i].department == "HR":
                wk.append(self.managers[i].show_manager_info())
        
        
        for i in range(len(self.employees)):
            if self.employees[i].department == "HR":
                wk.append(self.employees[i].show_employee_info())
        # return print(f"Workers of {self.departments[0]}: ", wk)
    
    def ux_workers(self):
        wk = []

        print(f"Workers of {self.departments[1]}: ")

        for i in range(len(self.managers)):
            if self.managers[i].department == "UX":
                wk.append(self.managers[i].show_manager_info())
        
        for i in range(len(self.employees)):
            if self.employees[i].department == "UX":
                wk.append(self.employees[i].show_employee_info())
        # return print(f"Workers of {self.departments[1]}: ", wk)
    
    def qa_workers(self):
        wk = []
        print(f"Workers of {self.departments[2]}: ")
              
        for i in range(len(self.managers)):
            if self.managers[i].department == "QA":
                wk.append(self.managers[i].show_manager_info())
        
        for i in range(len(self.employees)):
            if self.employees[i].department == "QA":
                wk.append(self.employees[i].show_employee_info())
        # return print(f"Workers of {self.departments[2]}: ", wk)
        
    def se_workers(self):
        wk = []
        print(f"Workers of {self.departments[3]}: ")

        for i in range(len(self.managers)):
            if self.managers[i].department == "Software Engineering":
                wk.append(self.managers[i].show_manager_info())
        
        for i in range(len(self.employees)):
            if self.employees[i].department == "Software Engineering":
                wk.append(self.employees[i].show_employee_info())
        # return print(f"Workers of {self.departments[3]}: ", wk)
    
    def pm_workers(self):
        wk = []
        print(f"Workers of {self.departments[4]}: ")

        for i in range(len(self.managers)):
            if self.managers[i].department == "Product management":
                wk.append(self.managers[i].show_manager_info())
        
        for i in range(len(self.employees)):
            if self.employees[i].department == "Product management":
                wk.append(self.employees[i].show_employee_info())
        # return print(f"Workers of {self.departments[4]}: ", wk)

managers = []
employees = []
company1 = Company(managers, employees)
company1.add_employee(Employees("Petr", "Vasilyevich", "80", "HR"))
company1.add_employee(Employees("Petr1", "Vasilyevich1", "23", "QA"))
company1.add_employee(Employees("Petr2", "Vasilyevich2", "30", "UX"))
company1.add_employee(Employees("Petr3", "Vasilyevich3", "43", "Software Engineering"))
company1.add_employee(Employees("Petr4", "Vasilyevich4", "27", "Product management"))
company1.add_manager(Managers("Vlad", "Lutsenko", "45", "Software Engineering"))
company1.add_manager(Managers("Kiril", "Lutsenko", "51", "UX"))
company1.add_manager(Managers("Petr5", "Vasilyevich5", "30", "UX"))
company1.add_manager(Managers("Petr6", "Vasilyevich6", "41", "HR"))
company1.add_manager(Managers("Petr7", "Vasilyevich7", "35", "Product management"))
print(company1.workers())
dep = Departments(company1.manager, company1.employee)
dep.hr_workers()
dep.qa_workers()
dep.ux_workers()
dep.se_workers()
dep.pm_workers()



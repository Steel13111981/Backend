from person import Person

class Employee(Person):
    years_experience = 0 
    programm_langs = []

    def __init__(self, experience = 0, programm_langs = [], **kwargs):
        Person.__init__(self, **kwargs)
        self.years_experience = experience
        self.programm_langs = programm_langs
        #print(experience)

    def get_first(self):
        name=self.get_first_name()
        return name
 

Maxim_employee = Employee(first_name="Maxim", last_name="Lukovets", experience=8, programm_langs=["Python", "HTML"])
Petro_employee = Employee(first_name="Petro", last_name="Petrenko", experience=10, programm_langs=["Java", "C++"])
#print(Maxim_employee.programm_langs)
#print(Petro_employee.years_experience)
#print(Maxim_employee.get_first())
from person import Person
from employee import Employee

class Client(Person):
    project_name = ""

    def __init__(self, project_name, **kwargs):
        Person.__init__(self, **kwargs)
        self.project_name=project_name

    def get_name(self):
        return self.first_name + ' ' + self.last_name + " client " + self.project_name


Petro_client = Client(first_name="Petro", last_name="Petrenko", project_name="I")
#print(Petro_client.get_name())

Maxim_employee = Employee(first_name="Maxim", last_name="Lukovets", experience=8, programm_langs=["Python", "HTML"])

persons = [Petro_client, Maxim_employee]
for person in persons:
    print(person.get_name())
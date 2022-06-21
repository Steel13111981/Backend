class Person():
    first_name = ""
    last_name = ""

    def __init__(self, first_name, last_name):
       self.first_name=first_name
       self.last_name=last_name
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_first_name(self):
        return self.first_name

    def get_name(self, str_after=""):
        name=self.get_first_name()
        return name + ' ' + self.last_name + " name" + str_after


Maxim_person = Person(first_name="Maxim", last_name="Lukovets")
Petro_person = Person(first_name="Petro", last_name="Petrenko")
#print(Maxim_person.first_name)
#print(Petro_person.last_name)
#print(Maxim_person)
#print(Maxim_person.get_first_name())
#print(Petro_person.get_name(" Is my name"))
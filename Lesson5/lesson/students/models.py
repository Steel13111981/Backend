from tabnanny import verbose
from django.db import models


class StudentGroup(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    
    students_number = models.DecimalField(max_digits=4, decimal_places=0, 
                                            verbose_name="Кол-во студентов",
                                             blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Группа студентов"
        verbose_name_plural = "Группы студентов"

class Student(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100, 
                                blank=True, null=True)

    birthday = models.DateField(verbose_name="День рождения", 
                                null=True, blank=True)

    group = models.ForeignKey(StudentGroup, verbose_name="Группа", on_delete=models.SET_NULL, 
                                null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name += '1111'
        
        
        super().save(*args, **kwargs)
        

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

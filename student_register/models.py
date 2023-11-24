""" Project Models """
from django.core.validators import RegexValidator
from django.db import models

just_letters = RegexValidator(r'^[a-zA-Z ]+$', 'Just letters allowed')
curp = RegexValidator(r'[a-zA-z0-9]+$')

# Create your models here.
class Student_Personal_Data(models.Model):
    curp = models.CharField(max_length=18, validators=[curp], primary_key=True)
    father_lastname = models.CharField(max_length=20, validators=[just_letters])
    mother_lastname = models.CharField(max_length=20, validators=[just_letters])
    names = models.CharField(max_length=40, validators=[just_letters])
    SEX_CHOICE = (
        ("F", "F"),
        ("M", "M")
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    birth_date = models.DateField()

    def __str__(self):
        return self.title


class Career_Profile(models.Model):
    career_id = models.CharField(max_length=5, primary_key=True)
    full_name = models.CharField(max_length=100)
    contraction = models.CharField(max_length=7)
    without_pressure = models.BooleanField(default=True)
    lenght_in_months = models.IntegerField()

class Student_Academic_Profile(models.Model):
    register_number = models.AutoField(primary_key=True) #REMEBER TO SET AUTOFIELD INITIAL VALUE IN MYSQL
    career = models.ForeignKey(Career_Profile, on_delete= models.CASCADE)
    student = models.ForeignKey(Student_Personal_Data, on_delete= models.CASCADE)

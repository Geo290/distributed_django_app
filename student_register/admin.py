from django.contrib import admin
from student_register import models

# Register your models here.
admin.site.register(models.Student_Personal_Data)
admin.site.register(models.Student_Academic_Profile)
admin.site.register(models.Career_Profile)

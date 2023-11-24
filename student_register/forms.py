"""Project form"""
from django import forms
from .models import Student_Personal_Data, Career_Profile, Student_Academic_Profile

class Personal_Data_Form(forms.ModelForm):
    class Meta:
        model= Student_Personal_Data
        fields = ['curp', 'father_lastname', 'mother_lastname', 'names', 'sex', 'birth_date']
        labels = {
            'father_lastname' : "Father's lastname",
            'mother_lastname' : "Mother's lastname",
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }
        validators = '__all__'
    def __init__(self, *args, **kwargs):
        super(Personal_Data_Form, self).__init__(*args, **kwargs)
        self.fields['sex'].empty_label = "Select"


class Career_Profile_Form(forms.ModelForm):
    class Meta:
        model = Career_Profile
        fields = '__all__'

  
class Academic_Profile_Form(forms.ModelForm):
    class Meta:
        model = Student_Academic_Profile
        fields = '__all__'
  
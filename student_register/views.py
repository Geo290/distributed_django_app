""" Project Views """
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Personal_Data_Form
from .models import Student_Personal_Data

# Create your views here.
def Student_List(request):
    context = {'student_list' : Student_Personal_Data.objects.all()}
    return render(request, "student_register/student_list.html", context)

def Student_Form(request, curp=""):
    if request.method == 'GET':
        if curp == "":
            form = Personal_Data_Form()
        else:
            student = get_object_or_404(Student_Personal_Data, pk=curp)
            form = Personal_Data_Form(instance=student)
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        if curp == "":
            form = Personal_Data_Form(request.POST)
        else:
            student = Student_Personal_Data.objects.filter(pk=curp).first()
            if student is None:
                return HttpResponseNotFound("Student not found")  # Handle this case appropriately
            form = Personal_Data_Form(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/list')
    return render(request, "student_register/student_form.html", {'form': form})

def Student_Delete(request, curp):
    student = Student_Personal_Data.objects.get(pk=curp)
    student.delete()
    return redirect('/list')
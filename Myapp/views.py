from django.shortcuts import render
from Myapp.forms import StudentForm
def home(request):
    stud= StudentForm
    return render(request,'index.html',{'form': stud})

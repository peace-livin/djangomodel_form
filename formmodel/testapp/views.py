from django.shortcuts import render
from testapp.models import student
# Create your views here.

def student_view(request):
    stu_list = student.objects.all()
    return render(request,'testapp/student.html',{'stu_list':stu_list})

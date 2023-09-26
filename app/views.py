from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"admin.html")
def s(request):
    return render(request,"staff.html")
def stu(request):
    return render(request,"student.html")

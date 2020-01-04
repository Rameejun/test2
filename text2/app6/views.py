from django.shortcuts import render
from app6.forms import *
# Create your views here.
def post(request):
    form = employeeform()
    if request.method == "POST":
        form = employeeform(request.POST)
        if form.is_valid():
            eid = form.cleaned_data["eid"]
            name = form.cleaned_data["name"]
            print(eid,name)
    return render(request,"home/form5.html",{"form":form})
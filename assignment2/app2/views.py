from django.shortcuts import render
from django.shortcuts import HttpResponse
def showmain(request):
    return render(request,"main.html")
def showindex(request):
    a=request.POST.get("t1")
    b=request.POST.get("t2")
    c= request.POST.get("a1")

    if c=="add":
        result=int(a)+int(b)
        return render(request,"main.html",{"data":result})
    if c=="sub":
        result=int(a)-int(b)
        return render(request,"main.html",{"data":result})
    if c=="mul":
        result=int(a)*int(b)
        return render(request,"main.html",{"data":result})
    if c=="div":
        result=int(a)/int(b)
        return render(request,"main.html",{"data":result})



# Create your views here.

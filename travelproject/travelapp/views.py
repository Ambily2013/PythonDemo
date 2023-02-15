from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.

def demo(request):

    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
#def about(request):
 #   return render(request,"about.html")
#def contact(request):
 #   return HttpResponse("hello am contact")
#def operations(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
#    add=x+y
 #   mul=x*y
  #  div=x/y
   # sub=x-y
    #return render(request,"result.html",{'a':add,'m':mul,'d':div,'s':sub})
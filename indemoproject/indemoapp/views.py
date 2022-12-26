from django.shortcuts import render
from.models import place
from .models import team

# Create your views here.
def demo(request):
    obj1=team.objects.all()
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1})
# def addition(request):
    # x=int(request.GET['num1'])
    # y=int(request.GET['num2'])
    # add=x+y
    # sub=x-y
    # mul=x*y
    # div=x/y
    #
    # return render(request,'result.html',{'add':add,'sub':sub,'mul':mul,'div':div})

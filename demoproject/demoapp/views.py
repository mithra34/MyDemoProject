from django.http import HttpResponse
from django.shortcuts import render
from  .models import  Place
from  .models import Team
# # Create your views here.
# def home(request):
#     return HttpResponse("I AM HOMEPAGE")
# def  about(request):
#     return HttpResponse("I AM ABOUT")
# def  contact(request):
#     return HttpResponse("CONTACT PAGE")
# def  detail(request):
#     return HttpResponse("DETAILS")
# def  thanks(request):
#     return HttpResponse("THANKYOU VISITING MY PAGE")
def demo(request):
    # return render(request,"result.html")
    obj=Place.objects.all()
    objt=Team.objects.all()

    return  render(request,"index.html",{'result':obj,'res':objt})
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add1=x+y
#     mul1 = x * y
#     sub1 = x - y
#     div1 = x / y
#     return render(request,"new.html",{'obj1':add1,'obj3':mul1,'obj2':sub1,'obj4':div1})
#
# def sub(request):
#     x=int(request.get['num1'])
#     y=int(request.get['num2'])
#     sub1=x-y
#
#     return render(request,'result.html',{'obj2':sub1})
# def mul(request):
#     x=int(request.get['num1'])
#     y=int(request.get['num2'])
#     mul1=x*y
#     return render(render(request,'result.html',{'obj3':mul1}))
# def div(request):
#     x = int(request.get['num1'])
#     y = int(request.get['num2'])
#     div1=x/y
#     return render(render(request, 'result.html', {'obj4': div1}))



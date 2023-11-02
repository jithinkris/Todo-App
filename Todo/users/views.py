from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.

@csrf_exempt
def home(request):
    request.session.flush()
    return render(request,'home.html',{})

@csrf_exempt
def login(request):
    data={}
    if request.POST:
        phone=request.POST.get("ID")
        Password=request.POST.get("Password")
        try:
            ob=User.objects.get(Phone=phone,Password=Password)
            request.session["phone"]=ob.Phone
            return UserHome(request)
        except Exception as e:
            data["status"]=False
    

    return render(request,'home.html',data)

@csrf_exempt
def register(request):
    phone=request.GET.get("phone")
    name=request.GET.get("name")
    pass1=request.GET.get("pass")
    data={}
    if request.GET:
        try:
            ob=User.objects.create(Name=name,Phone=phone,Password=pass1)
            data["status"]=True
        except Exception as e:
            data["status"]=False
            print(data)
    return render(request,'registration.html',data)



####################################################################################### USER SIDE ######################################################################

@csrf_exempt

def UserHome(request):
    Phone=request.session["phone"]
    try:
        data={}
        datalist=[]
        ob=Todolist.objects.filter(phone=Phone)
        for i in ob:
            data1={
                'title':i.title,
                'desc':i.desc,
                'duedate':i.duedate,
                'id':i.id,
                'status':True if i.status==1 else False
            }
            datalist.append(data1)
        data["data"]=datalist
      
        return render(request,"listview.html",data)

    except Exception as e:
        return render(request,"listview.html",{})

def ADDTODO(request):
    Phone=request.session["phone"]
    if request.GET:
        try:
            title=request.GET.get("tit")
            desc=request.GET.get("desc")
            duedate=request.GET.get("due")
            user=User.objects.get(Phone=Phone)

            Todolist.objects.create(phone=user,title=title,desc=desc,duedate=duedate,status=0)
            print("insert")
            return render(request,"AddNew.html",{'data' : True})
        except Exception as e:
            print(e)
            return render(request,"AddNew.html",{'data' : False})
    return render(request,"AddNew.html",{})


def editing(request):
    id=request.GET.get("id")
    title=request.GET.get("title")
    desc=request.GET.get("desc")
    duedate=request.GET.get("date")

    try:
        ob=Todolist.objects.get(id=id)
        ob.title=title
        ob.desc=desc
        ob.duedate=duedate
        ob.save()
    except Exception as e:
        print(e)
    return UserHome(request)



def delete(request):
    id=request.GET.get("ph")
    try:
        ob=Todolist.objects.get(id=id)
        ob.delete()
    except Exception as e:
        print(e)
    return UserHome(request)
def Done(request):
    id=request.GET.get("ph")
    try:
        ob=Todolist.objects.get(id=id)
        ob.status=1
        ob.save()
    except Exception as e:
        print(e)
    return UserHome(request)

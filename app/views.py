from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint
from .utils import *
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def JSPage(request):
    return render(request,"app/JS.html")

def homepage(request):
    if "email" in request.session and "role" in request.session:
        if request.session['role']=="employee":
            return render(request,"app/home.html")

def LoginPage(request):
    return render(request,"app/login.html")


def RegisterUser(request):
    try:
        if request.POST['role']=="employee":
            role = request.POST['role']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            phone = request.POST['phone']
            gender = request.POST['gender']
            image = request.FILES['image']

            user = User.objects.filter(email=email)

            if user:
                message = 'This email already exists'
                return render(request,"app/index.html",{'message':message})
            else:
                if password==cpassword:
                    otp = randint(100000,9999999)
                    newuser = User.objects.create(email=email,password=password,otp=otp,role=role)
                    newemp = Employee.objects.create(user_id=newuser,firstname=fname,
                    lastname=lname,phone=phone,gender=gender,image=image)
                    email_subject = "Employee Verifaction Mail"
                    sendmail(email_subject,'mail_template',email,{'name':fname,'otp':otp})

                    return render(request,"app/Success.html")
                else:
                    message = 'Password Doesnot match'
                    return render(request,"app/index.html",{'message':message})
        
    except Exception as e1:
        print("*************Register Exception************",e1)


def LoginUser(request):
    print("-----------Login User Method ---------------")
    try:
        if request.POST['role']=="employee":
            print("------------1-----------")
            email = request.POST['email']
            password = request.POST['password']

            user = User.objects.get(email=email)
        if user:
            print("------------------2-------------")
            if user.password == password and user.role == "employee":
                print("------------3----------------")
                emp = Employee.objects.get(user_id=user)
                request.session['email'] = user.email
                request.session['password'] = user.password
                request.session['firstname'] = emp.firstname
                request.session['lastname'] = emp.lastname
                request.session['role'] = user.role

                return render(request,"app/home.html")
            else:
                message = "Your password Doesnot Match"
                return render(request,"app/login.html",{'message':message})
        else:
            message = "User doesnot Exists"
            return render(request,"app/login.html",{'message':message})
            
    except Exception as e2:
        print("Login Exception-------------->",e2)
   

def logout(request):
    del request.session['email']
    del request.session['password']
    del request.session['firstname']
    del request.session['lastname']

    return HttpResponseRedirect(reverse('loginpage'))
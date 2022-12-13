from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from django.contrib.auth.models import Group

# Create your views here.
admingrp=Group.objects.get(name='admin')
customergrp=Group.objects.get(name="customer")



class RegistrationView(View):
    def get(self, request, ):
        uform = UserForm()
        pform = ProfileForm()
        return render(request,"registration.html",{"uform":uform,"pform":pform})

    def post(self, request,):
        uform = UserForm(request.POST)
        pform = ProfileForm(request.POST)
        role = request.POST['role']
        print(role)
        if uform.is_valid() and pform.is_valid():
            userobj = uform.save()
            # below mehtod use to encrept  the password.
            userobj.set_password(userobj.password)
            userobj.save()
            profileobj = pform.save(commit=False)
            profileobj.user = userobj
            profileobj.save()
            if role=="admin":
                userobj.groups.add(admingrp)
            elif role=="customer":
                userobj.groups.add(customergrp)   
            return redirect('/index') 
        return render(request,"registration.html",{"uform":uform,"pform":pform})

class LoginView(View):
    form = AuthenticationForm()
    def get(self,request):
        return render(request,'login.html',{'form':self.form})
        
    def post(self,request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user= authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"LOGIN SUCCESSFULLY")
            return redirect('/index')
        else:
            messages.error(request,"INVALID USER")
            return redirect('/account/login')

def LogoutView(request):
    print("thank Your",request.user)
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect("/index")


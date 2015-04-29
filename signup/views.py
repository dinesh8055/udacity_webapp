from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import re

welcome_name=""
def find(pat,string):
    match=re.search(pat,string)
    if(match):
         return match.group()
    else:
         return None

def validate_un(name):
    pat=(r"^[a-zA-Z0-9_-]{3,20}$")
    return find(pat,name)

def validate_password(pwd):
    pat=(r"^[\s\S]{3,20}$")
    return find(pat,pwd)

def validate_verify_password(pwd,ver_pass):
    if(pwd==ver_pass):
        return pwd
    else:
        return None

def validate_email(email):
    pat=(r"^[\w.-]+@[\w.-]+$")
    return find(pat,email)
        
def form(request):
    def write_form(name="",name_error="",password_error="",password_mismatch="",email_error="",email=""):
        return render(request,"signup/form.html",{"name":name,
                                                  "name_error":name_error,
                                                  "password_error":password_error,
                                                  "password_mismatch":password_mismatch,
                                                  "email_error":email_error,
                                                  "email":email})

    if(request.method=="GET"):
        return write_form()
    if(request.method=="POST"):
        un=request.POST.get('user_name','')
        global welcome_name
        welcome_name=un
        password=request.POST.get('password','')
        verify_password=request.POST.get('verify_password','')
        email=request.POST.get('email','')

        is_valid_un=validate_un(un)
        is_valid_password=validate_password(password)
        is_valid_verify_password=validate_verify_password(password,verify_password)
        is_valid_email=validate_email(email)

        password_mismatch=""
        email_error=""
        name_error=""
        password_error=""
        name=un
        if not(is_valid_un and is_valid_password and is_valid_verify_password):
            if not is_valid_un:
                name_error="Invalid user name"
            if not is_valid_password:
                password_error="Invalid password"
            if not(is_valid_verify_password or not(password)):
                    password_mismatch="Password Mismatch"
            if not(is_valid_email or not(email)):
                email_error="Invalid E-mail address"
            return write_form(un,name_error,password_error,password_mismatch,email_error,email)
        else:
            return HttpResponseRedirect('thanks')
    
def thanks_handler(request):
    string="Welcome, "+welcome_name+"!"
    return render(request,"signup/thanks.html",{'string':string})

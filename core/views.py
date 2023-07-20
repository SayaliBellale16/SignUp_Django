from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .form import  *
from django.contrib import messages
# Create your views here.
def home(request):
    return  render(request,'core/home.html')

class SignupView(View):
    def get(self,request):
        fm=SignUpForm()
        return render(request, 'core/signup.html',{'form':fm})
    def post(self,request):
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Sign Up Success !")
            return redirect('/signup')
        else:
            return render(request, 'core/signup.html', {'form': fm})
# def signupView(request):
#     return render(request,'core/signup.html')
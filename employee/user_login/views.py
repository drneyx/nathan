from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import auth
from django.contrib.auth import get_user_model


def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        emailaddress = request.POST.get('emailaddress','')
        password = request.POST.get('password','')


        #authenticate the user
        crispy_forms_tags = auth.authenticate(request,username = emailaddress, password=password)

        if form is not None:

            #go to login account
            auth.login(request,form)
            form = OrderReceivingForm()
            response= render('/employee_register/employee_form.html',{'form':form})

            #cookie to transfer the names to login success page
            response.set_cookie('emailaddress',emailaddress,3600)
            return response
        else:
            error_json = {'error_message': 'emailaddress or password is not correct.'}
            return render(request, 'user_login/login.html', error_json, {'form':form})
    else:
        form = UserForm()
        return render(request, 'user_login/login.html', {'form':form})

def register(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "user_login/register.html", {'form':form})
    else:
        if request.method == "POST":
            form = UserForm()
        #check whether the user account exist
            emailaddress = request.POST.get('emailaddress','')
            password = request.POST.get('password','')
            form = auth.authenticate(request, username = emailaddress, password = password)

        #if the user account do not exist
            if form is None:
                form = get_user_model().objects.create_user(username=emailaddress, password=password)
                if form is not None:
                    form.is_staff = True
                    form.save()
                response = redirect('/employee/user_list')
                request.session['emailaddress'] = emailaddress
                request.session['password'] = password
                return response
            else:
                error_json = {'error_message': 'User account exist, please register another one.'}
                return render(request, 'user_login/register.html', error_json)
        else:
             return render(request, 'user_login/register.html')



def user_list(request):
    context = {'user_list':User.objects.all()}
    return render(request, "user_login/success.html")

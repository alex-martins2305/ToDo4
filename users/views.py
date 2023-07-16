from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from ToDo4 import settings

def login(request):
    print("Base dir2 = ", settings.BASE_DIR2)
    print("STATICFILES_DIRS = ", settings.STATICFILES_DIRS)
    #print("STATIC_FILES = ", settings.STATICFILES_DIRS)
    
    print("STATIC_URL = ", settings.STATIC_URL)

    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method=='POST':
            email_user=request.POST['email_user']
            password=request.POST['password']
            if email_user=="" or password== "":
                messages.error(request, 'Para fazer Login é necessário digitar seu endereço de email ou nome de usuário.')
                return redirect('login')
            if User.objects.filter(username=email_user).exists():
                name=User.objects.filter(username=email_user).values_list('username', flat=True).get()
                user=auth.authenticate(request, username=name, password=password)
                if user is not None:
                    auth.login(request, user)
                return redirect('dashboard')
            else:
                if User.objects.filter(email=email_user).exists():
                    name=User.objects.filter(email=email_user).values_list('username', flat=True).get()
                    user=auth.authenticate(request, username=name, password=password)
                    if user is not None:
                        auth.login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Verifique seu login e senha.')
                    return redirect('login')
        else:
            return render(request, 'users/login.html')
        
def logout(request):
    print ('logout')
    auth.logout(request)
    return redirect('login')

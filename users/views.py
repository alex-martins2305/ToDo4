from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method=='POST':
            email_user=request.POST['email_user']
            password=request.POST['password']
            print(email_user, "  ", password)
            if email_user=="" or password== "":
                messages.error(request, 'Para fazer Login é necessário digitar seu endereço de email ou nome de usuário.')
                return redirect('login')
            if User.objects.filter(username=email_user).exists():
                print("achei nome")
                name=User.objects.filter(username=email_user).values_list('username', flat=True).get()
                user=auth.authenticate(request, username=name, password=password)
                if user is not None:
                    auth.login(request, user)
                return redirect('dashboard')
            else:
                if User.objects.filter(email=email_user).exists():
                    print("achei email")
                    name=User.objects.filter(email=email_user).values_list('username', flat=True).get()
                    user=auth.authenticate(request, username=name, password=password)
                    if user is not None:
                        auth.login(request, user)
                    return redirect('dashboard')
                else:
                    print('nem nome nem email')
                    messages.error(request, 'Verifique seu login e senha.')
                    return redirect('login')
        else:
            return render(request, 'users/login.html')
        
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html' )
    else:
        return redirect ('login')

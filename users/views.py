from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from ToDo4 import settings

def login(request):
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

def signup (request):
    if request.method == 'POST':
        nome = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if nome!="" and email!="":
            if email.count('@')==1:
                if len(password1)>=6:
                    if password1==password2:
                        if User.objects.filter(email=email).exists() or User.objects.filter(username=nome).exists():
                            messages.error(request, 'Já existe um usuário cadastrado com esse nome ou com esse email.')
                            return render (request, 'users/signup.html')
                        else:
                            user=User.objects.create_user(username=nome, email=email, password=password1)
                            user.save()
                            auth.login(request, user)
                            return redirect('dashboard')
                    else:
                        messages.error(request, 'Suas senhas devem ser iguais')
                        return render (request, 'users/signup.html')
                else:
                    messages.error(request, 'Sua senha deve ter no mínimo 6 caracteres.')
                    return render (request, 'users/signup.html')
            else:
                messages.error(request, 'Digite um email válido.')
                return render (request, 'users/signup.html')
        else:
            messages.error(request, 'Nome e email não podem ser vazios')
            return render (request, 'users/signup.html')
    else:
        return render (request, 'users/signup.html')
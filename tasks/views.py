from django.shortcuts import render, redirect

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'tasks/dashboard.html' )
    else:
        return redirect ('login')
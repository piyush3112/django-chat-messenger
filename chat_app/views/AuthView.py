from django.shortcuts import render, redirect
from chat_app.forms import SignUpForm
from django.contrib.auth.models import User

def login_redirect(request):
    if request.user.is_authenticated():
        return redirect('/messenger')
    else:
        return redirect('/login')

def signup(request):
    if request.method == 'POST':
        print("----1")
        form = SignUpForm(request.POST)
        print("----2")
        if form.is_valid():
            print("---3")
            form.save()
            print("---4")
            return redirect('/login')
    else:
        form = SignUpForm()
        args = {'form' : form}
        return render(request, 'chat_app/signup.html', args)




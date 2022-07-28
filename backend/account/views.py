from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from account.forms import SignupForm


# Create your views here.


    

def signup(request):
    form =SignupForm(request.POST)
    if request.method == 'POST':
        form =SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            raw_password =form.cleaned_data.get('password1')
            user =authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('home')
    
        else:
            messages.info(request, 'Cannot sign up. Please, refill the form correctly') 
    context = {'form': form}
    return render(request, 'signup.html', context)



def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
                messages.error(request,'Username Or Password Is Incorrect')

    context = {} 
    return render(request, 'login.html', context)  



def userlogout(request):
    logout(request)
    return redirect('home')
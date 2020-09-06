from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method =="POST":
			form = RegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request,"Account has been successfully created. Please login below")
				return redirect('login')

			# return redirect("/")
		else:
			form = RegistrationForm()

		return render(request,"register.html",{"form":form})




def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		
		context  ={}
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username = username, password =password)

			if user is not None:
				login(request,user)
				return redirect("home")
			else:
				messages.info(request," Username OR Password is incorrect.")

		return render(request,"login.html",context)


def logoutUser(request):
	logout(request)
	return redirect('login')
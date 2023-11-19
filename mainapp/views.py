from django.shortcuts import render, get_object_or_404, redirect
from .models import SMS
from .forms import SMSForm
import requests
from django.contrib.auth.decorators import login_required

@login_required
def sms_list(request):
    sms_list = SMS.objects.all()
    return render(request, 'sms_list.html', {'sms_list': sms_list})

@login_required
def sms_detail(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    return render(request, 'sms_detail.html', {'sms': sms})

@login_required
def sms_new(request):
    if request.method == "POST":
        form = SMSForm(request.POST)
        if form.is_valid():
            sms = form.save(commit=False)
            sms.save()
            send_sms(sms.to_number, sms.message)
            messages.success(request, "Message sent successfully" )
            return redirect('sms_detail', pk=sms.pk)
    else:
        form = SMSForm()
    return render(request, 'index.html', {'form': form})

@login_required
def sms_edit(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    if request.method == "POST":
        form = SMSForm(request.POST, instance=sms)
        if form.is_valid():
            sms = form.save(commit=False)
            sms.save()
            send_sms(sms.to_number, sms.message)
            messages.success(request, "Message Edited successfully" )
            return redirect('sms_detail', pk=sms.pk)
    else:
        form = SMSForm(instance=sms)
    return render(request, 'index.html', {'form': form})

@login_required
def sms_delete(request, pk):
    sms = get_object_or_404(SMS, pk=pk)
    sms.delete()
    messages.success(request, "Message Deleted" )

    return redirect('sms_list')

def send_sms(to_number, message):
    api_key = "q2fTLzxo4m7KwO0ctcnTICwuCv0UJHKoK7XEOIjZW8xXoVCgP5Px9fK1NlT0"
    base_url = "https://www.fast2sms.com/dev/bulkV2"

    headers = {
        "authorization": api_key,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }

    payload = {
        "route": "q",
        "message": message,
        "language": "english",
        "numbers": to_number,
    }

    response = requests.post(base_url, headers=headers, json=payload)
    print(response.text)

# def index(request):
#     return render(request,"index.html")
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

from django.shortcuts import  render, redirect
from .forms import NewUserForm,CustomAuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

def login_request(request):
	if request.method == "POST":
		form = CustomAuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("sms_new")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = CustomAuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("register")
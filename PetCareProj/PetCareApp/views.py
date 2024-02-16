from django.db import models
from django.shortcuts import render,redirect
import requests
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Pets



def index(request):
    return render(request, 'index.html')
def donate(request):
    return render(request, 'donate.html')
# def chatbot(request):
#     return render(request, 'chatbot.html')
    
def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        api_key = "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"
        url = "https://api.perplexity.ai/chat/completions"

        payload = {
            "model": "pplx-70b-online",  # Replace with your desired model
            "messages": [
                {
                    "role": "system",
                    "content": "Be precise and concise."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            completion = response.json()
            solution = completion['choices'][0]['message']['content'] if 'choices' in completion else "No solution found"
            return render(request, 'chatbot.html', {'user_input': user_input, 'solution': solution})
        else:
            error_message = f"Error: {response.status_code}"
            return render(request, 'chatbot.html', {'user_input': user_input, 'error_message': error_message})

    return render(request, 'chatbot.html')



def login (request):
    if request.method == 'POST':
        userid = request.POST['petid'] 
        password = request.POST['password'] 

        user=auth.authenticate(username=userid,password=password)

        if user is not None:
            # User is authenticated, log them in
            auth.login(request,user)
            return redirect('index')  
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')




def registration (request):
    if request.method == 'POST':
        petname = request.POST['petname']  # Assuming 'userid' is the email
        petid= request.POST['petid']  # Assuming 'userid' is the email
        petage = request.POST['petage']  # Assuming 'userid' is the email
        petgender = request.POST['gender']  # Assuming 'userid' is the email
        password = request.POST['password']  # Assuming 'password' is the registration number

        user=User.objects.create_user(username=petid, password=password)
        user.save()
        pets = Pets.objects.create(
            petname=petname,
            petid=petid,
            petage=petage,
            petgender=petgender,
            password=password
            
        )
        #write above like model feilds 


        return render(request, 'login.html')

    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('login')  
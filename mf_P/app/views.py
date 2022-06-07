from django.db.models.fields import json
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

import time
from datetime import datetime, timedelta
from django.utils import timezone

from app.models import token, ariza_E
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import arizaSerializer

from django.views import generic

#from .forms import arizaForm

import requests
import json


def homePage(request):
    global data_global
    token_list = token.objects.get()
    pinfl = 32208996860027
    
    url1 = "http://ministry.hemis.uz/app/rest/v2/oauth/token"
    url2 = "http://ministry.hemis.uz/app/rest/v2/services/student/get?pinfl=" + str(pinfl)
    
    time_now = timezone.now()
    time_token = token_list.token_created
    token_expires = token_list.expires_in

    # difference
    total_second = time_now - time_token
    difference = total_second.total_seconds()
    

    if token_expires < difference:
        payload1 = {'grant_type': 'password',
                'username': 'moliya',
                'password': 'isYAa2R6z9dP9YV'}
        files1 = [

        ]
        headers1 = {
        'Authorization': 'Basic Y2xpZW50OnNlY3JldA=='
        }

        response1 = requests.request("POST", url1, headers=headers1, data=payload1, files=files1)
        
        data1 = json.loads(response1.text)
        
        token1 = data1['access_token']
        expires = data1['expires_in']
        token_list.token = token1
        token_list.token_created = timezone.now()
        token_list.expires_in = expires
        token_list.save()
        # print(response1.text)
    else:
        payload2 = {}
        headers2 = {
            'Authorization': 'Bearer ' + token_list.token
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
        data_global = json.loads(response2.text)
        #print(data2['success']) 

        # print(response2.text)
    return render(request, 'home.html')

@login_required(login_url='login')
def indexPage(request):
    return render(request, 'index.html')

def arizaPage(request):
    context = {}
    
    data = data_global['data']
    # print(data_global)
    context = {
        'firstname': data['firstname'],
        'lastname': data["lastname"],
        'fathername': data["fathername"]
    }
        
    return render(request, 'ariza.html', context)


# def formPage(request):
#     token_list = token.objects.get()
#     url = "http://ministry.hemis.uz/app/rest/v2/services/student/get?pinfl=32208996860027"
#
#     payload={}
#     headers = {
#         'Authorization': 'Bearer ' + token_list.token
#     }
#
#     response2 = requests.request("GET", url, headers=headers, data=payload)
#
#     data = json.loads(response2.text)
#     data1 = data["data"]
#
#     context = {
#         'data_s': data["success"],
#         'data_p': data1["pinfl"],
#         'data_n': data1["firstname"],
#         'data_l': data1["lastname"],
#         'data_f': data1["fathername"],
#         'data_b': data1["birthday"]
#     }
#
#     print(response2.text)
#     return render(request, 'form-elements-component.html', context)

def aboutPage(request):
    return render(request, 'about.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged out!')
    return redirect('home')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Unknown Account, Please re-enter!') 

    return render(request, 'login.html', {})

def regPage(request):
    form = UserCreationForm()
    context = {}
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    context['form'] = form
    return render(request, 'register.html', context)


def token_time_check(token):
    time_elapsed = timezone.now() - token.created
    return time_elapsed
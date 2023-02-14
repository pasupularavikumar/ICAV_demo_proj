from django.shortcuts import render

# Create your views here.
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm  
from .forms import *
from .models import *
from django.contrib.sessions.models import Session
from django.utils import timezone 
 
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import *
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user  = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, "login.html")

@login_required(login_url='login')
def home(request):
    username = request.user
    books = Book.objects.all()
    context ={'books':books,'username':username}
    return render(request,'home.html',context )

@login_required(login_url='login')
def addbook(request):
    username = request.user
    form = BookForm
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')        
    context ={ 'form':form,'username':username }
    return render(request, "addbook.html",context)

    
@login_required(login_url='login')
def updatebook(request, id): 
    username = request.user 
    c_book = Book.objects.get(id = id)
    obj = get_object_or_404(Book, id = id)
    form = BookForm(request.POST or None, instance = obj)  
    if form.is_valid():  
        form.save()  
        return redirect("home")  
    context = {"form":form, 'username':username, "c_book":c_book}
    return render(request, "updatebook.html", context)


def logout_view(request):
    logout(request)
    return redirect('login')


class bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = bookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
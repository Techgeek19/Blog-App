from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import generic
from .models import *
from .forms import loginform,registerform, postform
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def register(request):
    if request.method=='POST':
        form= registerform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            first_name= form.cleaned_data.get('first_name')
            last_name= form.cleaned_data.get('last_name')
            email= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password')
            cpassword = form.cleaned_data.get("confirm_password")
            user = User.objects.create_user(username=username, first_name= first_name, last_name =last_name, email=email, password=password)
            user.save(); 
            messages.success(request,'Registered successfully..Login here')
            return redirect('/login/')
    return render (request, 'register.html', {'form': registerform})

def login(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            try:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect ('/post/')
                else: 
                    messages.warning(request,'Invalid Credentials')

            except ObjectDoesNotExist:
                print("invalid user") 
    return render (request,'login.html', context={'form': loginform})

def postview(request):
    if request.method=='POST':
        form=postform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Created')
    else:
        form= postform()
    return render (request,'postform.html', context={'form': form})
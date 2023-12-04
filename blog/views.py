from django.shortcuts import render,HttpResponseRedirect
from blog.models import Post
from django.contrib.auth.models import Group
from blog.forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

#   <--------========*******|||||   Start Home page   |||||*******=======------->    #
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts' : posts})
#   <--------========*******|||||   End Home page   |||||*******=======------->    #



#   <--------========*******|||||   Start About page   |||||*******=======------->    #
def about(request):
    return render(request, 'blog/about.html')
#   <--------========*******|||||   End About page   |||||*******=======------->    #



#   <--------========*******|||||   Start Contact page   |||||*******=======------->    #
def contact(request):
    return render(request, 'blog/contact.html')
#   <--------========*******|||||   End Contact page   |||||*******=======------->    #



#   <--------========*******|||||   Start Dashboard page   |||||*******=======------->    #
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()

        return render(request, 'blog/dashboard.html', {'posts' : posts, 'full_name' : full_name, 'groups' : gps})
    else:
        return HttpResponseRedirect('/login/')
#   <--------========*******|||||   End Dashboard page   |||||*******=======------->    #



#   <--------========*******|||||   Start Logout page   |||||*******=======------->    #
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
#   <--------========*******|||||   End Logout page   |||||*******=======------->    #



#   <--------========*******|||||   Start Signup page   |||||*******=======------->    #
def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations...! You have become an author. ")
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form' : form})
#   <--------========*******|||||   End Signup page   |||||*******=======------->    #



#   <--------========*******|||||   Start Login page   |||||*******=======------->    #
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']

                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in succesfully..!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form' : form})
    else:
        return HttpResponseRedirect('/dashboard/')
#   <--------========*******|||||   End Login page   |||||*******=======------->    #


#   <--------========*******|||||   Start Add New Post   |||||*******=======------->    #

def add_post(request):
    if request.user.is_authenticated:
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "New post added succesfully ...!!")
                return HttpResponseRedirect('/dashboard/')
                form = PostForm()
            else:
                form = PostForm()
        return render (request, 'blog/addpost.html', {'form' : form})
    else:
        return HttpResponseRedirect('/login/')
    
#   <--------========*******|||||   End Add New Post   |||||*******=======------->    #


#   <--------========*******|||||   Start Edit Post   |||||*******=======------->    #

def edit_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request, "Post updated succesfully ...!!")
                return HttpResponseRedirect('/dashboard/')

        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render (request, 'blog/editpost.html', {'form' : form})
    else:
        return HttpResponseRedirect('/login/')
    
#   <--------========*******|||||   End Edit Post   |||||*******=======------->    #

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            messages.success(request, "Post deleted succesfully ...!!")
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
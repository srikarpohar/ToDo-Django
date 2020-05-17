from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']

        x= User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        context = {'todo_list': Todo.objects.all()}
        return render(request, 'homepage.html',context)
    else:
        return render(request, 'signup.html')

def loginuser(request):
    if(request.method == 'POST'):
        username1 = request.POST['username']
        password1 = request.POST['password']
        x= authenticate(username=username1,password=password1)
        if x is None:
            return render(request, 'signup.html')
        else:
            login(request,x)
            try:
                context={'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
            except:
                context = {'todo_list': []}
            return render(request, 'homepage.html', context)
    else:
        if request.user.is_authenticated:
            try:
                context = {'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
            except:
                context = {'todo_list': []}
            return render(request, 'homepage.html',context)
        else:
            return render(request, 'login.html')

def todo_list(request, id):
    context = {'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
    return render(request, "homepage.html", context)

def add_task(request, id=0):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(pk=id)
            todo = Todo(user_id=user)
            form = TodoForm(request.POST,instance=todo)
            if form.is_valid():
                form.save()
            try:
                context = {'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
            except:
                context = {'todo_list': []}
            return render(request,'homepage.html',context)
        else:
            form = TodoForm(request.POST)
            return render(request, "newtask.html", {'form': form})
    else:
        return render(request, 'login.html')

def update_task(request, user_id=0, task_id=0):
    if request.user.is_authenticated:
        if request.method == "GET":
            user = User.objects.get(pk=user_id)
            todo = Todo(user_id=user,pk=task_id)
            form = TodoForm(request.POST,instance=todo)
            return render(request, "updatetask.html", {"form":form, "task_id":task_id})
        else:
            user = User.objects.get(pk = user_id)
            todo = Todo(user_id = user, pk = task_id)
            form = TodoForm(request.POST,instance = todo)
            if form.is_valid():
                form.save()
            try:
                context = {'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
            except:
                context = {'todo_list': []}
            return render(request, 'homepage.html', context)
    else:
        return render(request, 'login.html')

def delete_task(request, user_id=0, task_id=1):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = User.objects.get(pk = user_id)
            todo = Todo(user_id = user, pk = task_id)
            todo.delete()
            try:
                context = {'todo_list': Todo.objects.filter(user_id_id=request.user.id).values()}
            except:
                context = {'todo_list': []}
            return render(request, 'homepage.html', context)
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return render(request, 'login.html')





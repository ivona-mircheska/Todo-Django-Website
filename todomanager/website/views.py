from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Task
from .forms import SignUpForm, TaskForm
# from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)   
            messages.success(request, "You Have Been Loged In!") 
            return redirect('home')
        else:
            messages.success(request, "Invalid Username or Password!")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
            return render(request, 'home.html', {'tasks': tasks})
        else:
            return render(request,'home.html')
    

def logout_user(request):
    logout(request)
    messages.success(request,"You Have Been Logged Out!")
    return redirect('home')


def register_user(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})



def create_task(request):
    if request.user.is_authenticated:
        form = TaskForm(request.POST or None)
        if request.method=='POST':
            if form.is_valid():
                task = form.save(commit=False)
                task.user=request.user
                task.save()
                messages.success(request, "Task Created!")
                return redirect('home')
        
        return render(request,'create_task.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to create a task!")
        return redirect('home')
    
def delete_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        task.delete()
        messages.success(request, "Task Deleted!")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In!")
        return redirect('home')


def update_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        if task.user!=request.user:
            messages.success(request, "You can only update your own tasks!")
            return redirect('home')
        form = TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            task = form.save(commit= False)
            task.user = request.user
            task.save()
            if task.task_status in ["Finished", "Done", "finished", "done"]:
                return redirect('finished')
            messages.success(request, "Task Updated!")
            return redirect('home')
        
        
        return render(request, 'update_task.html', {'form':form})
    else:
        messages.success(request,"You must be logged in to create a task!")
        return redirect('home')

def finished_tasks(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user, task_status__in=['Finished', 'Done'])
        return render(request, 'finished_tasks.html', {'tasks': tasks})
    else:
        return redirect('home')

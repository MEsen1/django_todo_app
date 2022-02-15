from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def home(request):
   
    return render(request,'todo/home.html')



def todo_list(request):
    todos = Todo.objects.all()
    
    context = {
        'todos' : todos    
    }
    
    return render(request,'todo/todo_list.html',context)



def todo_add(request):
    form = TodoForm();
    
    if request.method =='POST':
        #!take all data assert inside form
        form = TodoForm(request.POST)
        if form.is_valid():
            #! valid then save db
            form.save();
            return redirect('todo_list')
    context={
                'form':form
            }       
    return render(request,'todo/todo_add.html',context)

def todo_detail(request,id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo' : todo
    }
    
    return render(request,'todo/todo_detail.html',context)

def todo_update(request,id):
    todo = Todo.objects.get(id=id)
    #! fill out form with given date
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save();
            return redirect('todo_list')
    context = {
        'todo' : todo,
        'form' : form
    }
    
    return render(request, 'todo/todo_update.html',context)


def todo_delete(request,id):
    todo = Todo.objects.get(id=id)
    #!delete is also a post
    if request.method == 'POST':
        todo.delete();
        return redirect('todo_list')
    context = {
        'todo' : todo
    }
    
    return render(request,'todo/todo_delete.html',context)

<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
=======
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
>>>>>>> 8aedc00d3b14aa44351c0a82e58953b17759622c
from .models import Todo

class TodoListView(ListView):
    model = Todo
<<<<<<< HEAD
    template_name = "todos/todo_list.html"
    context_object_name = "todos"

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Buscar usuário pelo email
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog')
            else:
                messages.error(request, 'Credenciais inválidas')
        except User.DoesNotExist:
            messages.error(request, 'Usuário não encontrado')
    
    return render(request, 'todos/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password', '')
        
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem')
            return render(request, 'todos/cadastro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está cadastrado')
            return render(request, 'todos/cadastro.html')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este usuário já existe')
            return render(request, 'todos/cadastro.html')
        
        # Criar usuário
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=nome
        )
        
        messages.success(request, 'Conta criada com sucesso! Faça seu login.')
        return redirect('login')
    
    return render(request, 'todos/cadastro.html')

@login_required
def blog_view(request):
    return render(request, 'todos/blog.html')

def logout_view(request):
    logout(request)
    return redirect('login')
=======
    template_name = "todos/todo_list.html"  
    context_object_name = "todos"           
        
class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "description"]
    success_url = reverse_lazy("todo_list")
>>>>>>> 8aedc00d3b14aa44351c0a82e58953b17759622c

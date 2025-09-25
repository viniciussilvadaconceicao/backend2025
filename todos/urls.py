from django.urls import path
<<<<<<< HEAD
from .views import TodoListView, login_view, cadastro_view, blog_view, logout_view

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("", login_view, name="login"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("blog/", blog_view, name="blog"),
    path("logout/", logout_view, name="logout"),
]
=======
from todos.views import TodoListView, TodoCreateView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create")
]
  
>>>>>>> 8aedc00d3b14aa44351c0a82e58953b17759622c

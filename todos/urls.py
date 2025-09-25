from django.urls import path
from .views import TodoListView, login_view, cadastro_view, blog_view, logout_view

urlpatterns = [
    path("todos/", TodoListView.as_view(), name="todo_list"),
    path("", login_view, name="login"),
    path("cadastro/", cadastro_view, name="cadastro"),
    path("blog/", blog_view, name="blog"),
    path("logout/", logout_view, name="logout"),
]
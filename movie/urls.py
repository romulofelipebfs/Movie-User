
from django.urls import path
from . import views



urlpatterns = [
    path("", views.FilmeList.as_view(), name=""),
    path("movie-create", views.FilmeView.as_view()),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('user-logout', views.user_logout, name="user-logout"),

    path('favoritar/<int:filme_id>', views.toggle_favorito, name='toggle-favorito')
]

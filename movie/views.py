from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView

from movie.forms import FilmeForm, CreateUserForm, LoginForm
from movie.models import Filme

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url="my-login")
def toggle_favorito(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)

    if filme.favoritado_por.filter(id=request.user.id).exists():
        filme.favoritado_por.remove(request.user)
    else:
        filme.favoritado_por.add(request.user)
    return redirect("")   


 
class FilmeList(ListView):
    template_name = "movie/index.html"
    model = Filme
    context_object_name = "filmes"


class FilmeView(CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = "movie/movie-create.html"
    success_url = "/"

def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("my-login")


    return render(request, "movie/register.html", {
        'form':form
    })



def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data = request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")



    return render(request, "movie/my-login.html", {
        "form":form
    })

def user_logout(request):

    auth.logout(request)
    
    return redirect("")

@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'movie/dashboard.html')
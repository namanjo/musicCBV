from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import Album, Song
from .forms import UserForm, LoginForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = "music/index.html"

    def get_queryset(self):
        return Album.objects.all()


@method_decorator(login_required, name='dispatch')
class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"


@method_decorator(login_required, name='dispatch')
class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


@method_decorator(login_required, name='dispatch')
class SongCreate(CreateView):
    model = Song
    fields = ['file_name', 'album', 'audio_file']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):           #For Sign Up
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


class ForLogin(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # context = {}

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # if user:
        #     if user:
        #         login(request, user)
        #         return redirect('music:index')
        #     else:
        #         context['error'] = "DO properly mate"
        #         return render(request, self.template_name, context)
        # else:
        #     context = {"error": "Provide Valid Credentials", "form": form}
        #     return render(request, self.template_name, context)
        if user:
            login(request, user)
            return redirect('music:index')
        else:
            context = {"error": "Provide Valid Credentials", "form": form}
            return render(request, self.template_name, context)


class ForLogout(View):
    form_class = LoginForm
    template_name = 'music/login_form.html'

    def get(self, request):
        logout(request)

        # form = LoginForm(request.GET or None)
        # return render(request, self.template_name, context={'form': form})

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # context = {}

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('music:index')
        else:
            context = {"error": "Provide Valid Credentials", "form": form}
            return render(request, self.template_name, context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Aktirovka, Workers, Appeal, Text
from django.views.generic import DetailView
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import Group
from django.views.generic import FormView
from .forms import AppealForm


def index(request):
    news = News.objects.all()
    return render(request, 'homepage/index.html', {'news': news})


def aktirovka(request):
    aktirovka = Aktirovka.objects.all()
    return render(request, 'homepage/aktirovka.html', {'aktirovka': aktirovka})


def workers(request):
    workers = Workers.objects.all()
    return render(request, 'homepage/workers.html', {'workers': workers})


def appeal(request):
    appeal = Appeal.objects.all()
    return render(request, 'homepage/appeal.html', {'appeal': appeal})


class NewsDetailView(DetailView):
    model = News
    template_name = 'homepage/details_news.html'
    context_object_name = 'news_detail'


class AktirovkaDetailView(DetailView):
    model = Aktirovka
    template_name = 'homepage/details_aktirovka.html'
    context_object_name = 'aktirovka_detail'


class WorkersDetailView(DetailView):
    model = Workers
    template_name = 'homepage/details_workers.html'
    context_object_name = 'workers_detail'


class RegisterFormView(FormView): # Форма для регистрации нового пользователя
    form_class = UserCreationForm
    success_url = '../login'

    template_name = 'homepage/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.groups.add(Group.objects.get(name='user'))
        new_user.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView): # Форма для авторизации нового пользователя
    form_class = AuthenticationForm
    success_url = "../"

    template_name = "homepage/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View): # Форма для выхода из аккаунта
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("../")


def create(request):
    error = ''
    if request.method == 'POST':
        form = AppealForm(request.POST)
        if form.is_valid():
            text1 = Text(text=form.cleaned_data['text'])
            text1.save()
            ref = Appeal(user=request.user, title=form.cleaned_data['title'], text=text1)
            ref.save()
        else:
            error='Ошибка заполнения формы'
    form = AppealForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'homepage/appeal.html', data)

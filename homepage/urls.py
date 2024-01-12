from . import views
from django.urls import path, include

urlpatterns = (
    path('', views.index, name='news'),
    path('aktirovka/', views.aktirovka, name='aktirovka'),
    path('workers/', views.workers, name='workers'),
    path('appeal/', views.create, name='appeal'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('aktirovka/<int:pk>/', views.AktirovkaDetailView.as_view(), name='aktirovka-detail'),
    path('workers/<int:pk>/', views.WorkersDetailView.as_view(), name='workers-detail'),
    path('register', views.RegisterFormView.as_view(), name='register'),
    path('login', views.LoginFormView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
)

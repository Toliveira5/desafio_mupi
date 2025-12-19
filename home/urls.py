from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landpage, name='landpage'),

    path('mensagem/enviar/', views.enviar_mensagem, name='enviar_mensagem'),
    path('mensagem/enviada/', views.mensagem_enviada, name='mensagem_enviada'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

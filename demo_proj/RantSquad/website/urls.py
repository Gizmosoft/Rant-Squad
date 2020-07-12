from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='website-index'),
    # path('login/', views.login, name='website-login'),
    # path('register/', views.register, name='website-register'),
    path('profile/', views.profile, name='website-profile'),
]

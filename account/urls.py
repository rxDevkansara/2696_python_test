
from django.urls import path
from . import views

urlpatterns = [
    path('registration',views.regirstion, name='regirastion'),
    path('login',views.user_login, name='login'),
]

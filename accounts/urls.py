from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='shoes/home.html'),name='logout'),
]
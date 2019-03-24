from django.urls import path
from shoes import views

urlpatterns=[
    path('nike/',views.nike,name='nike'),
    path('adidas/',views.adidas,name='adidas'),
    path('details/',views.details,name='details'),
]
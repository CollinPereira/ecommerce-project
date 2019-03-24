from django.urls import path
from shoes import views

urlpatterns=[
    path('nike/',views.nike,name='nike'),
    path('adidas/',views.adidas,name='adidas'),
    path('puma/',views.puma,name='puma'),
    path('<int:shoe_id>/',views.details,name='details'),
]
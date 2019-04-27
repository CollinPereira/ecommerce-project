from django.urls import path
from .views import ShoesListView
from shoes import views

urlpatterns=[
    # path('nike/',views.nike,name='nike'),
    path('nike/',ShoesListView.as_view(),name='nike'),
    path('adidas/',views.adidas,name='adidas'),
    path('puma/',views.puma,name='puma'),
    path('<int:shoe_id>/',views.details,name='details'),
]
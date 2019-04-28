from django.urls import path
from .views import NikeListView , SearchListView ,AdidasListView,PumaListView
from shoes import views

urlpatterns=[
    # path('nike/',views.nike,name='nike'),
    path('nike/',NikeListView.as_view(),name='nike'),
    path('search/',SearchListView.as_view(),name='search'),
    path('adidas/',AdidasListView.as_view(),name='adidas'),
    path('puma/',PumaListView.as_view(),name='puma'),
    path('<int:shoe_id>/',views.details,name='details'),
]
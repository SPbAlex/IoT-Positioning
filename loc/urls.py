from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('units/', views.UnitPageView.as_view(), name='units'),

    path('req', views.vote, name='vote'),

    path('get_coords/', views.coords, name='coords'),
]

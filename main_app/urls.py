from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create')


]
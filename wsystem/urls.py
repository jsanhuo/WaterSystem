from django.urls import path

from . import views
app_name = 'wsystem'
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
]
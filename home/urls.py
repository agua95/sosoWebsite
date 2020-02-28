from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='index'),
    path('<int:tutorial_id>/', views.details, name="detail")
]
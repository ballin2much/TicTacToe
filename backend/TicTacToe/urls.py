from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from django.urls import path
import TicTacToe.views as views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('make-move/', views.make_move),
]

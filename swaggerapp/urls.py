from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
 path('',views.InfoView.as_view()),
 path('info/<int:pk>',views.AdvanceView.as_view()),
]

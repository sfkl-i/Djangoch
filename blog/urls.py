from . import views
from django.urls import path

urlpatterns = [
    path('category/<slug:slug>/', views.Category_View.as_view(), name = 'category'),
    path("", views.HomeView.as_view()),
]
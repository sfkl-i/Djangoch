from . import views
from django.urls import path

urlpatterns = [
    path("<slug:category_name>/", views.Category_View.as_view(), name = 'category'),
    path("", views.HomeView.as_view()),
]
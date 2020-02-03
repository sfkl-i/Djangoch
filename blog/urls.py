from . import views
from django.urls import path

urlpatterns = [
    path('<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path("", views.HomeView.as_view()),
    path('<slug:category>/<slug:slug>', views.PostDetailView.as_view(), name='detail_post')
]


from django.shortcuts import render

from django.views.generic.base import View

from .models import Category, Post


class HomeView(View):
    """Home page"""
    def get(self, request):
        category_list = Category.objects.all()
        print(category_list)
        return render(request, "blog/home.html", {'categories': category_list})

class Category_View(View):
    """Вывод статей категории"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {'category': category})

class PostDetailView(View):
    """Вывод постов категории"""
    def get(self,request,category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, "blog/post_list.html", {'category': category})

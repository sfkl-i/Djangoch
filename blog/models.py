from django.db import models

class Category(models.Model):
    """Модель категорий"""
    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    """Моедль тегов"""
    name = models.CharField(verbose_name='Имя тега', max_length=100, unique=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    published = models.BooleanField("Отображать?", default=True)


class Post(models.Model):
    """Модель постов"""
    title = models.CharField("Заголовок", max_length=100)
    mini_text = models.TextField("Краткое содержание", max_length=5000)
    text = models.TextField("Текст", max_length=10000000)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=100, unique=True)

class Comment(models.Model):
    """Модель комментариев"""
    text = models.TextField("Текст комментария")
    created_date = models.DateTimeField("Дата создания", auto_now=True)
    moderation = models.BooleanField(default=True)


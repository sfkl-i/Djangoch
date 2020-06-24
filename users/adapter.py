from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from blog import views
from django.urls import path

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        return path("<slug:category>/<slug:slug>/", views.PostDetailView.as_view(), name="detail_post")

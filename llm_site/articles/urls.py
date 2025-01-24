"""
URL configuration for llm_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
app_name = "articles"
urlpatterns = [
    path("", views.articles, name="articles"),
    path("<int:pk>/", views.article_detail, name="article_detail"),
    path("create/", views.create, name="create"),
    path("hello/", views.hello, name="hello"),
    path("data-throw/", views.data_throw, name="throw"),
    path("data-catch/", views.data_catch, name="catch"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/update/", views.update, name="update"),
]

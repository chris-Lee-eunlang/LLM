# my_first_pjt/articles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

def hello(request):
	context = {"name": "수연"}
	return render(request, "articles:hello.html", context)

def data_throw(request):
	return render(request, "articles:data_throw.html")

def data_catch(request):
		message = request.GET.get("message")
		context = {
				"data" : message,
		}
		return render(request, "articles:data_catch.html", context)

from .models import Article

def articles(request):
    articles = Article.objects.all().order_by("-id")
    context = {
        "articles": articles,
    }
    return render(request, "articles:articles.html", context)

from.forms import ArticleForm

@login_required
def create(request):
  if request.method == "POST":
      form = ArticleForm(request.POST)
      if form.is_valid():
          article = form.save()
          return redirect("articles:article_detail", article.id)
  else:
      form = ArticleForm()

  context = {"form": form}
  return render(request, "articles:create.html", context)


def article_detail(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
      "article": article,
  }
  return render(request, "articles:article_detail.html", context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
      article.delete()
      return redirect("articles:articles")
  return redirect("articles:article_detail", article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:article_detail", article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        "form": form,
        "article": article,
    }
    return render(request, "articles:update.html", context)
# from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
    CreateView,
    FormView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import SingleObjectMixin


# Create your views here.

from .models import ArticlesModel
from .forms import CommentForm


class ArticleListView(LoginRequiredMixin, ListView):
    model = ArticlesModel
    context_object_name = "articles"
    template_name = "article_list.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticlesModel
    fields = ["title", "body"]
    template_name = "article_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentGet(DetailView):
    model = ArticlesModel
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = ArticlesModel
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    context_object_name = "article"
    model = ArticlesModel
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "article"
    model = ArticlesModel
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    context_object_name = "article"
    model = ArticlesModel
    template_name = "article_update.html"
    fields = ["title", "body"]

    def test_func(self):
        """
        docstring
        """
        obj = self.get_object()
        return obj.author == self.request.user

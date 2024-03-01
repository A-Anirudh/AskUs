from .models import Log, Comments, Like, Solutions
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.views.generic.edit import FormMixin
from django.core.exceptions import PermissionDenied
from .forms import CommentForm



class VerificationRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        print('hi',self.get_object())
        if self.get_object:
            post = self.get_object()
            if self.request.user == post.author:
                if EmailAddress.objects.get(user=self.request.user).verified == True:
                    return super().dispatch(request, *args, **kwargs)
                else:
                    print('Not verified')
                    send_email_confirmation(self.request, self.request.user)
                    return redirect('log-detail', question=post.slug)
            else:
                raise PermissionDenied()
        else:
            if EmailAddress.objects.get(user=self.request.user).verified == True:
                return super().dispatch(request, *args, **kwargs)
            else:
                print('Not verified')
                send_email_confirmation(self.request, self.request.user)
                return redirect('home')


class VerificationEmailForAddMixin:
    def dispatch(self, request, *args, **kwargs):
        if EmailAddress.objects.get(user=self.request.user).verified == True:
            return super().dispatch(request, *args, **kwargs)
        else:
            print('Not verified')
            send_email_confirmation(self.request, self.request.user)
            return redirect('home')

        

class LogListView(ListView):
    model = Log
    template_name = 'log/home.html'
    context_object_name = 'item'
    ordering = ['-created']

class LogDetailView(DetailView):
    model = Log
    slug_url_kwarg = 'question'
    slug_field = 'slug'

    

class LogCreateView(LoginRequiredMixin, VerificationEmailForAddMixin, CreateView):
    model = Log
    fields = ['title', 'content', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LogUpdateView(LoginRequiredMixin, VerificationRequiredMixin, UpdateView):
    model = Log
    fields = ['title', 'content', 'image']
    slug_url_kwarg = 'question'
    slug_field = 'slug'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class SolutionDetailView(FormMixin, DetailView):
    model = Solutions
    template_name = 'log/solution.html'
    slug_url_kwarg = 'solution'
    slug_field = 'slug'
    context_object_name = 'solution'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comments.objects.all()
        return context

    def get_success_url(self):
        return reverse('log-solution', kwargs={'solution':self.kwargs['solution']}
)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
            comments = form.save(commit=False)
            comments.author = self.request.user
            comments.log = self.object
            comments.save()            
            return super(SolutionDetailView, self).form_valid(form)


class SolutionsCreateView(LoginRequiredMixin,VerificationEmailForAddMixin, CreateView):
    model = Solutions
    fields = ['solution', 'image']
    template_name = "log/add_solution.html"
    slug_url_kwarg = 'solution'
    slug_field = 'slug'
    context_object_name = 'solution'
    
    def form_valid(self, form):
        log = Log.objects.get(slug=self.kwargs['question'])
        form.instance.author = self.request.user
        form.instance.log = log
        return super(SolutionsCreateView, self).form_valid(form)
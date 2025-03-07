from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from App1.models import Posts

class CreatePost(CreateView):
    model = Posts
    template_name = 'main.html'
    fields = ['Title', 'bodyText', 'author', 'status']
    success_url = reverse_lazy("success")

class Success(TemplateView):
    template_name = 'success.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        posts = Posts.objects.all()
        context['posts'] = posts
        return self.render_to_response(context)
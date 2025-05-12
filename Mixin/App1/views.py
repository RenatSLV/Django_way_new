from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .mixin import LoginRequiredMixinPlus

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixinPlus, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

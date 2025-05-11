from django.views.generic import ListView
from blog.models import Post

class PostView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Post
from django.db.models import F


class HomeView(View):
    template_name = "main/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BlogView(View):
    template_name = "main/blog.html"

    def get(self, request, *args, **kwargs):
        data = Post.objects.values("created_at__date__year").values(year=F("created_at__date__year")).distinct()
        result = {}
        for item in data:
            year = item["year"]
            result[str(year)] = Post.objects.filter(created_at__date__year=year)

        # Extract all posts for the default case
        all_posts = Post.objects.all().order_by('-created_at')

        context = {
            'result': result,
            'all_posts': all_posts,
        }
        return render(request, self.template_name, context)

class ArticleView(View):
    template_name = 'main/article.html'

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        # Find the next post
        next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()

        # Find the previous post
        prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()

        context = {
            'post': post,
            'next_post': next_post,
            'prev_post': prev_post,
        }
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = 'main/about.html'

    def get(self, request):
        return render(request, self.template_name)
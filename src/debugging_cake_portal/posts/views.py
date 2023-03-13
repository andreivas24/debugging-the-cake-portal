import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from hitcount.views import HitCountDetailView
from comment.form import CommentForm
from comment.models import Comment
from django.core.paginator import Paginator
from like.models import Like
from notifications.models import Notification
from cake_user.models.user_model import User
from posts.models.post_model import Post
from .filters import PostFilter


def like_unlike_post(request):
    ok = True
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        if not created:
            if not like.value:
                like.value = True
            else:
                like.value = False
        else:
            like.value = False
        post_obj.save()
        like.save()
        if not like.value:
            notify = Notification(post=like.post, sender=like.user, user=like.post.author, notification_type=1)
            notifications = Notification.objects.filter(sender=like.user).order_by('-date')
            for noti in notifications:
                if noti.post == notify.post and noti.user == notify.user:
                    notify = Notification.objects.get(post=noti.post, sender=noti.sender)
                    notify.date = datetime.datetime.now()
                    notify.is_seen = False
            notify.save()
    return redirect('index')


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        page = self.request.GET.get('page', 1)
        paginator = Paginator(Post.objects.all(), 2)
        post_page_obj = paginator.get_page(page)
        page_range = paginator.get_elided_page_range(number=page)

        context = {'page_range': page_range, 'page': page, 'paginator': paginator, 'page_obj': post_page_obj}

        context.update({
            'filterset': self.filterset,
            'post_page_obj': post_page_obj
        })
        return context


# API REQUEST FACTORY

# Usage
class PostListView(FilteredListView):
    model = Post
    filterset_class = PostFilter
    paginate_by = 2
    template_name = 'postlist.html'
    ordering = ['-date_created']


def about_page(request):
    return render(request, 'about.html')


class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={'pk': int(post.id)}))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        user_count = User.objects.all().count()
        comment_count = Comment.objects.all().count()
        post_count = Post.objects.all().count()
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
            'user_count': user_count,
            'comment_count': comment_count,
            'post_count': post_count
        })

        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.request.FILES
        form.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'description', 'post_tag', 'file']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.request.FILES
        if form.is_valid():
            return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def onButtonClick(document=None):
    document.getElementById('textInput').className = "show"

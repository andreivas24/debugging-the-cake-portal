from django.shortcuts import render
from django.views.generic import DetailView
from rest_framework.generics import get_object_or_404

from posts.models import Post
from .models import Comment
from .form import CommentForm


class CommentView(DetailView):
    model = Post
    template_name = ""

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():

            try:
                content = form.cleaned_data['content']
            except:
                content = None

            try:
                parent = form.cleaned_data['parent']
            except:
                parent = None

            comment = Comment.objects.create(
                content=content, post=post
            )

            new_comment = Comment(content=content, author=self.request.user, CommentPost=self.get_object(),
                                  parent=parent)
            new_comment.save()

            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)
            # return redirect(self.request.path_info)

        return self.render_to_response(context=context)
        # return redirect(self.request.path_info)

from django.shortcuts import render,redirect
from .models import Comment
from django.http import HttpResponse

from .forms import CommentForm

def post_detailview(request):
    template_name='app1/post_details.html'

    if request.method == 'POST':
        cf = CommentForm(request.POST)
        if cf.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post = post, user = request.user, content = content)
            comment.save()
            return redirect(post.get_absolute_url())
        
        else:
            cf = CommentForm()
            context ={ 'comment_form':cf,}
        return render(request, template_name, context)

      
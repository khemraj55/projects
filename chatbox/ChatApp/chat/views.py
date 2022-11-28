from django.shortcuts import render, redirect

def chatPage(request, *args, **kwargs):
    templates='chat/chatPage.html'
    if not request.user.is_authenticated:
        return redirect("login-user")
    context={}
    return render(request,templates, context)
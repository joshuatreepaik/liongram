from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.generic import ListView

from .models import Post

def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')

def post_create_view(request):
    return render(request, 'posts/post_form.html')

def post_detail_view(request, id):
    return render(request, 'posts/post_detail.html')

def post_update_view(request,id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_confirm_delete.html')

# Create your views here.
def url_view(request):
    return HttpResponse('url_view')

def url_parameter_view(request, username):
    print('url_parameter_view')
    print(username)
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    print(f'request.GET: {request.GET}')
    print(f'request.POST: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model = Post
    template_name = "cbv_view.html"
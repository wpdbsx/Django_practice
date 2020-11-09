from django.views.generic import ListView
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse,HttpRequest
# Create your views here.

# post_list = ListView.as_view(model = Post)  # 클래스형

class ItemListView(ListView):
    model = Post
post_list = ItemListView.as_view()
# def post_list(request) :   # 함수형
#     qs = Post.objects.all()
#     q = request.GET.get('q','')
#     if q :
#         qs = qs.filter(message__icontains =q)
#     # instagram/templates/instagram/post_list.html
#     return render(request , 'instagram/post_list.html',{
#         'post_list': qs,
#         'q':q,
#     })

def post_detail(request: HttpResponse,pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello World") 
    return response
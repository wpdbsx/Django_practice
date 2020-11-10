from django.views.generic import ListView,DetailView
from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import HttpResponse, HttpRequest,Http404

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


# def post_detail(request: HttpResponse, pk: int) -> HttpResponse:
#     # try :
#     #     post = Post.objects.get(pk=pk) # DoesNotExist 예외
#     # except Post.DoesNotExist :
#     #     raise Http404
#     post = get_object_or_404(Post,pk=pk)
#     return render(request, "instagram/post_detail.html", {"post": post,})


# post_detail = DetailView.as_view(
    
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))
class PostDetailView(DetailView):
    model =Post
    # queryset = Post.objects.filter(is_public=True)
    def  get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated :
            qs = qs.filter(is_public=True)
        
            
        return qs
post_detail =  PostDetailView.as_view()    
def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")

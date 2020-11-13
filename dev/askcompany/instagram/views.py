from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,ArchiveIndexView,YearArchiveView
from django.shortcuts import render , get_object_or_404,redirect
from .models import Post
from django.http import HttpResponse, HttpRequest,Http404
from django.utils.decorators import method_decorator
from .forms import PostForm
# Create your views here.

def post_new(request):
    if request.method =='POST' :
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else :
        form = PostForm()
   
    return render(request,'instagram/post_form.html',{
        'form':form,
    })
    
# post_list = ListView.as_view(model = Post)  # 클래스형


# class ItemListView(ListView):
#     model = Post
#     paginate_by=10


# post_list = ItemListView.as_view()
# post_list = login_required(post_list)
########################################
@method_decorator(login_required,name = 'dispatch')
class PostListView(ListView):
    model = Post
    paginate_by =10
post_list=  PostListView.as_view()
########################################
# @login_required
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
# def archives_year(request, year):
#     return HttpResponse(f"{year}년 archives")


post_archive = ArchiveIndexView.as_view(model=Post , date_field ='created_at',paginate_by =10)

post_archive_year =YearArchiveView.as_view(model=Post,date_field='created_at',make_object_list=True)
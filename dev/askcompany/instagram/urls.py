from django.urls import path,re_path

from . import views
urlpatterns= [

    path('',views.post_list),
    path('<int:pk>/',views.post_detail), #int로 넘어감
    # re_path(r'(?P<pk>\d+)/$',views.post_detail),  #str로 넘어감
]

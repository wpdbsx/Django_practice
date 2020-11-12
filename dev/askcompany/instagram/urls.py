from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter,MonthConverter,DayConverter



register_converter(YearConverter, "year")
register_converter(MonthConverter, "month")
register_converter(DayConverter, "day")

app_name = "instagram"  # URL Reverse에서namespace역할을 한다.
urlpatterns = [
    path("", views.post_list,name="post_list"),
    path("<int:pk>/", views.post_detail,name="post_detail"),  # int로 넘어감
    # re_path(r'(?P<pk>\d+)/$',views.post_detail),  #str로 넘어감
    # path("archives/<int:year>/", views.archives_year),
    # re_path(r"archives/(?P<year>20\d{2})/", views.archives_year),
    # r 을쓰면 \ 를 자동 이스케이프 해준다.
    # path("archives/<year:year>/", views.archives_year),
    path ('archive/',views.post_archive, name='post_archive'),
    path('archive/<year:year>/',views.post_archive_year,name='post_archive_year'),
    # path('archive/<year:year>/<month:month>/',views.post_archive_month,name='post_archive_month'),
    # path('archive/<year:year>/<month:month>/<day:day>/',views.post_archive_day,name='post_archive_day'),
    
]

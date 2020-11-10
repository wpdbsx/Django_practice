from django.urls import path, re_path, register_converter

from . import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)  # 문자열을 정수로 바꿔주는것

    def to_url(self, value):
        return str(value)  # 문자를 url 문자열로 리버싱


register_converter(YearConverter, "year")

app_name = "instagram"  # URL Reverse에서namespace역할을 한다.
urlpatterns = [
    path("", views.post_list,name="post_list"),
    path("<int:pk>/", views.post_detail,name="post_detail"),  # int로 넘어감
    # re_path(r'(?P<pk>\d+)/$',views.post_detail),  #str로 넘어감
    # path("archives/<int:year>/", views.archives_year),
    # re_path(r"archives/(?P<year>20\d{2})/", views.archives_year),
    # r 을쓰면 \ 를 자동 이스케이프 해준다.
    path("archives/<year:year>/", views.archives_year),
]

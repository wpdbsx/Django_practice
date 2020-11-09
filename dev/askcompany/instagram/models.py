from django.db import models
import os
from uuid import uuid4
from django.utils import timezone
# Create your models here.

class Post(models.Model) :
    message = models.TextField()
    photo = models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False,verbose_name='공개 여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # JAVA의 toString
    def __str__(self):
        # return f"Custom Post object({self.id})"
        return self.message

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"
    # def uuid_name_upload_to(instance, filename):
    #     app_label = instance.__class__._meta.app_label # 앱 별로
    #     cls_name = instance.__class__.__name__.lower() # 모델 별로
    #     ymd_path = timezone.now().strftime('%Y/%m/%d') # 업로드하는 년/월/일 별로
    #     uuid_name = uuid4().hex
    #     extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
    #     return '/'.join([
    #     app_label,
    #     cls_name,
    #     ymd_path,
    #     uuid_name[:2],
    #     uuid_name + extension,
    #     ])

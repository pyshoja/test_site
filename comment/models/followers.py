from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from comment.managers.followers import FollowerManager


class Follower(models.Model):
    email = models.EmailField(verbose_name='ایمیل')
    username = models.CharField(max_length=50 , verbose_name='نام کاربری')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE , verbose_name='متن')
    object_id = models.PositiveIntegerField(verbose_name='آی دی')
    content_object = GenericForeignKey()

    objects = FollowerManager()

    class Meta:
        verbose_name='طرفدار'
        verbose_name_plural='طرفداران'

    def __str__(self):
        return f'{str(self.content_object)} followed by {self.email}'

    def __repr__(self):
        return self.__str__()

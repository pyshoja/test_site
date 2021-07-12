from django.db import models
from account.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# Create your models here.


# class Apiadress (models.Model):
#     api_adress = models.GenericIPAddressField(verbose_name='آدرس آی پی')
#
#     class Meta:
#         verbose_name = 'آی پی آدرس'
#         verbose_name_plural = 'آی پی آدرس ها'



class My(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='my_parented', verbose_name='نویسنده سایت')
    name_site = models.CharField(max_length=100, null=True, verbose_name='نام سایت')
    name_admin = models.CharField(max_length=100, null=True, verbose_name='نام و نام خانوادگی ادمین')
    time_start = models.DateTimeField(null=True, verbose_name='سال افتتاح سایت')
    title = models.CharField(max_length=200, null=True, verbose_name='مشهوریت سایت با نام')
    copy_site = models.CharField(max_length=200, null=True, verbose_name='توضیح در مورد جواز کپی از سایت')
    description = RichTextField(blank=True, null=True, verbose_name='توضیحات و معرفی درباره سایت')
    logo = models.ImageField(upload_to='my_images', verbose_name='لوگوی سایت')
    adress_admin = models.CharField(max_length=1000 , null=True , verbose_name='آدرس و موقعیت ')
    phone_admin = models.CharField(max_length=11 , null=True , verbose_name='شماره تماس ادمین ')
    email_admin = models.EmailField(max_length=100 , null=True , verbose_name='ایمیل ادمین ')

    class Meta:
        verbose_name = '* ادمین سایت *'
        verbose_name_plural = '* ادمین سایت *'

    def __str__(self):
        return self.name_site

    def get_absolute_url (self):
        return reverse('mylist')



class Category(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='category_parented', verbose_name='نویسنده')
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=100, null=True, verbose_name='عنوان')
    # slug = models.SlugField(max_length=100, unique=True, null=True, verbose_name='آدرس')
    # site = models.ManyToManyField("sites.Site", blank=True , verbose_name='سایت')
    description = RichTextField(blank=True, null=True, verbose_name='توضیحات')
    image = models.ImageField(upload_to='post_images', blank=True, null=True, verbose_name='عکس')
    status = models.BooleanField(null=True, verbose_name='نمایش برای کاربران عمومی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.parent and self.check_self_parent(self.parent):
            raise Exception('Invalid Move : A category may not be made a child of itself or any of its descendants.')
        return super(Category, self).save(*args, **kwargs)

    def check_self_parent(self, obj):
        if self == obj:
            return True
        if obj.parent:
            return self.check_self_parent(obj.parent)
        return False

    def get_absolute_url (self):
        return reverse('categorylist')


class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='parented', verbose_name='نویسنده')
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='زیر دسته' , related_name='parented')
    title = models.CharField(max_length=100, verbose_name='عنوان پست')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='آدرس')
    date = models.DateField(default=timezone.now, verbose_name='زمان پست')
    introduction = models.CharField(max_length=300, null=True, verbose_name='معرفی کوتاه')
    description = RichTextField(blank=True, null=True, verbose_name='توضیحات')
    image = models.ImageField(upload_to='post_images', verbose_name='عکس')
    status = models.BooleanField(default=True, verbose_name='نمایش برای کاربران عمومی')
    preview = models.BooleanField(default=True , verbose_name='پیش نویس')
    comments = GenericRelation(Comment)
    # hits = models.ManyToManyField(Apiadress, blank=True , related_name='hits', verbose_name='بازدیدها')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('postlist')



class Slider(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='slider_parented', verbose_name='نویسنده')
    title = models.CharField(max_length=100, verbose_name='عنوان اسلایدر')
    image = models.ImageField(upload_to='slid_images', verbose_name='عکس')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title

    def get_absolute_url (self):
        return reverse('sliderlist')



class support (models.Model):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    STATES_CHOICES = [
        (a, 'مالی سایت'),
        (b, 'آموزش ها'),
        (c, 'روند ثبت نام و ورود'),
        (d, 'پیگیری ها'),
        (e, 'متفرقه'),
    ]
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='support_parented', verbose_name='نویسنده')
    title_suppurt = models.IntegerField(choices=STATES_CHOICES , null=True , verbose_name='موضوع پیگیری')
    name_user = models.CharField(max_length=200 , null=True , verbose_name='نام و نام خانوادگی کاربر')
    phone_user = models.CharField(max_length=11 , null=True , verbose_name='شماره تماس کاربر ')
    email_user = models.EmailField(max_length=100 , null=True , verbose_name='ایمیل کاربر ')
    description_user = RichTextField(blank=True, null=True, verbose_name='توضیحات برای راهنمایی پشتیبانی سایت')

    class Meta:
        verbose_name = 'پشتیبانی سایت'
        verbose_name_plural = 'پشتیبانی سایت'

    def __str__(self):
        return self.title_suppurt

    def get_absolute_url (self):
        return reverse('supportlist')

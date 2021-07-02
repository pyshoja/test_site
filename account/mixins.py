from django.shortcuts import get_object_or_404
from django.http import Http404
from first_app.models import Post , Category

# محدود سازی فرم ایجاد مقاله
class fieldsMixinpost():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','parent','title','slug','introduction','description','image','status']

        elif request.user.is_author:
            self.fields = ['parent', 'title', 'slug', 'introduction', 'description', 'image', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به نویسندگی در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)

# محدود سازی فرم ایجاد دسته بندی
class fieldsMixincategory():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','parent','title','description','status']

        elif request.user.is_author:
            self.fields = ['parent', 'title', 'description', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به نویسندگی در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)

# ذخیره سازی مقاله های هر کاربر برای خودش
class formvalidMixin ():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user

        return super().form_valid(form)


# برای امنیت ورود به ویرایش های پست های ادمین
class authoraccessMixin():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(Post, pk= pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')


# برای امنیت ورود به ویرایش های دسته بندی های ادمین
class authoraccessMixincategory():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(Category, pk= pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')


# برای امنیت ورود به حذف پست ها فقط با سوپر ادمین
class superuseraccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : شما توانایی در حذف جزئیات سایت را ندارید و برای حذف باید با پشتیبانی سایت ارتباط برقرار کنید')

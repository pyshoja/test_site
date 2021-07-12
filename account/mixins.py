from django.shortcuts import get_object_or_404
from django.http import Http404
from first_app.models import Post , Category , My , Slider , support
from comment.models.comments import Comment

# محدود سازی فرم ایجاد مقاله
class fieldsMixinpost():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','preview','parent','title','slug','introduction','description','image','status']

        elif request.user.is_author:
            self.fields = ['parent','preview', 'title', 'slug', 'introduction', 'description', 'image', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به نویسندگی در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)

# محدود سازی فرم ایجاد دسته بندی
class fieldsMixincategory():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','parent','title','description','status']

        # elif request.user.is_author:
        #     self.fields = ['parent', 'title', 'description', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به ایجاد دسته بندی در سایت من را ندارید')

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


# محدود سازی فرم ایجاد درباره من
class fieldsMixinmy():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','name_site','name_admin','title','copy_site','description','logo','adress_admin','phone_admin','email_admin']

        # elif request.user.is_author:
        #     self.fields = ['parent', 'title', 'description', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به ایجاد درباره من در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)


# برای امنیت ورود به ویرایش های درباره من
class myauthoraccessMixin():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(My, pk= pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')



# محدود سازی فرم ایجاد اسلایدرها
class fieldsMixinslider():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title','author','image']

        # elif request.user.is_author:
        #     self.fields = ['parent', 'title', 'description', 'status']

        else:
            raise Http404('. هشدار : شما دسترسی به ایجاد اسلایدر ها در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)



# برای امنیت ورود به ویرایش های اسلایدر ها
class sliderauthoraccessMixin():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(Slider, pk= pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')



# محدود سازی فرم ایجاد پشتیبانی سایت
class fieldsMixinsupport():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','title_suppurt','name_user','phone_user','email_user','description_user']

        elif request.user:
            self.fields = ['title_suppurt', 'name_user', 'phone_user', 'email_user' , 'description_user']

        else:
            raise Http404('. هشدار : شما دسترسی به ایجاد پشتیبانی در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)



# برای امنیت ورود به ویرایش های پشتیبانی سایت
class supportauthoraccessMixin():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(support, pk= pk)
        if post.author == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')



# برای امنیت ورود به ویرایش های دیدگاه ها
class commentauthoraccessMixin():
    def dispatch(self, request,pk , *args, **kwargs):
        post = get_object_or_404(Comment, pk= pk)
        if post.user == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : درخواست شما غیر مجاز است')



# محدود سازی فرم ایجاد دیدگاه های سایت
class fieldsMixincomment():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['user','content']

        elif request.user:
            self.fields = ['content']

        else:
            raise Http404('. هشدار : شما دسترسی به ایجاد دیدگاه در سایت من را ندارید')

        return super().dispatch(request, *args, **kwargs)


# برای امنیت ورود به حذف دیدگاه ها
class useraccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404('. هشدار : شما توانایی در حذف جزئیات سایت را ندارید و برای حذف باید با پشتیبانی سایت ارتباط برقرار کنید')

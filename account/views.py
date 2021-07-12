from django.shortcuts import render
from account.models import User
from account.forms import profileform
from django.urls import reverse_lazy
from django.views.generic import (
                                  TemplateView ,
                                  ListView ,
                                  CreateView ,
                                  UpdateView ,
                                  DeleteView ,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
                     fieldsMixinpost ,
                     formvalidMixin ,
                     authoraccessMixin ,
                     superuseraccessMixin ,
                     fieldsMixincategory ,
                     authoraccessMixincategory ,
                     fieldsMixinmy ,
                     myauthoraccessMixin ,
                     fieldsMixinslider ,
                     sliderauthoraccessMixin ,
                     fieldsMixinsupport ,
                     supportauthoraccessMixin ,
                     commentauthoraccessMixin,
                     fieldsMixincomment,
                     useraccessMixin ,
                     )
from first_app.models import Post , Category , My , Slider , support
from comment.models.comments import Comment


# Create your views here.


class homeadmin (LoginRequiredMixin, TemplateView):
    template_name = 'admin_lte/home.html'

# قسمت مقالات ادمین سایت من
class postlist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/postlist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=self.request.user)


class postcreate (LoginRequiredMixin,formvalidMixin, fieldsMixinpost, CreateView):
    model = Post
    template_name = 'admin_lte/postcreate.html'


class postupdate (LoginRequiredMixin, authoraccessMixin, formvalidMixin, fieldsMixinpost, UpdateView):
    model = Post
    template_name = 'admin_lte/postcreate.html'


class postdelete (superuseraccessMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('postlist')
    template_name = 'admin_lte/postdelete.html'


# قسمت دسته بندی های ادمین سایت من
class categorylist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/categorylist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.all()
        else:
            return Category.objects.filter(author=self.request.user)


class categorycreate (LoginRequiredMixin,formvalidMixin, fieldsMixincategory, CreateView):
    model = Category
    template_name = 'admin_lte/categorycreate.html'


class categoryupdate (LoginRequiredMixin, authoraccessMixincategory, formvalidMixin, fieldsMixincategory, UpdateView):
    model = Category
    template_name = 'admin_lte/categorycreate.html'


class categorydelete (superuseraccessMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('categorylist')
    template_name = 'admin_lte/categorydelete.html'

# پروفایل
class profile (LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'admin_lte/profile.html'
    form_class = profileform
    success_url = reverse_lazy('profile')
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(profile, self).get_form_kwargs()
        kwargs.update({
            'user' : self.request.user
        })
        return kwargs


# درباره من
class mylist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/mylist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
                return My.objects.all()
        else:
            return My.objects.filter(author=self.request.user)


class mycreate (LoginRequiredMixin,formvalidMixin, fieldsMixinmy, CreateView):
    model = My
    template_name = 'admin_lte/mycreate.html'


class myupdate (LoginRequiredMixin, myauthoraccessMixin, formvalidMixin, fieldsMixinmy, UpdateView):
    model = My
    template_name = 'admin_lte/mycreate.html'


class mydelete (superuseraccessMixin, DeleteView):
    model = My
    success_url = reverse_lazy('mylist')
    template_name = 'admin_lte/mydelete.html'



# اسلایدر ها
class sliderlist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/sliderlist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
                return Slider.objects.all()
        else:
            return Slider.objects.filter(author=self.request.user)


class slidercreate (LoginRequiredMixin,formvalidMixin, fieldsMixinslider, CreateView):
    model = Slider
    template_name = 'admin_lte/slidercreate.html'


class sliderupdate (LoginRequiredMixin, sliderauthoraccessMixin, formvalidMixin, fieldsMixinslider, UpdateView):
    model = Slider
    template_name = 'admin_lte/slidercreate.html'


class sliderdelete (superuseraccessMixin, DeleteView):
    model = Slider
    success_url = reverse_lazy('sliderlist')
    template_name = 'admin_lte/sliderdelete.html'







# پشتیبانی سایت
class supportlist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/supportlist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
                return support.objects.all()
        else:
            return support.objects.filter(author=self.request.user)


class supportcreate (LoginRequiredMixin,formvalidMixin, fieldsMixinsupport, CreateView):
    model = support
    template_name = 'admin_lte/supportcreate.html'


class supportupdate (LoginRequiredMixin, supportauthoraccessMixin, formvalidMixin, fieldsMixinsupport, UpdateView):
    model = support
    template_name = 'admin_lte/supportcreate.html'


class supportdelete (superuseraccessMixin, DeleteView):
    model = support
    success_url = reverse_lazy('supportlist')
    template_name = 'admin_lte/supportdelete.html'



# دیدگاه های سایت
class commentlist (LoginRequiredMixin, ListView):
    template_name = 'admin_lte/commentlist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
                return Comment.objects.all()
        else:
            return Comment.objects.filter(user=self.request.user)


# class commentcreate (LoginRequiredMixin,formvalidMixin, fieldsMixinsupport, CreateView):
#     model = Comment
#     template_name = 'admin_lte/supportcreate.html'


class commentupdate (LoginRequiredMixin, commentauthoraccessMixin, formvalidMixin, fieldsMixincomment, UpdateView):
    model = Comment
    template_name = 'admin_lte/commentcreate.html'


class commentdelete (useraccessMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('commentlist')
    template_name = 'admin_lte/commentdelete.html'
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
                     )
from first_app.models import Post , Category
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



from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView , DetailView , ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import registerForm
from django.contrib.auth.views import LoginView
from .models import My , Slider , Category , Post



class filter_author (ListView):
    template_name = 'pages/filter_description.html'
    model = Post

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        auth_id = self.kwargs.get('author_id')
        query = query.filter(author__id=auth_id)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


class description (LoginRequiredMixin , DetailView):
    model = Post
    template_name = 'pages/description.html'
    slug_field = 'id'
    context_object_name = 'my_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


class filter_category (ListView):
    template_name = 'pages/filter_description.html'
    model = Post

    def get_queryset(self, **kwargs):
        query = super().get_queryset(**kwargs)
        cat_id = self.kwargs.get('category_id')
        query = query.filter(parent__id=cat_id)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


class firstpageview (ListView):
    template_name = 'first_app/first_page.html'
    model = Post
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


class aboutview (TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        return context


class registerview (generic.CreateView):
    form_class = registerForm
    success_url = reverse_lazy('loginsite')
    template_name = 'registration/register.html'
    success_message = 'سلام خوش آمدید پیامک ثبت نام به ایمیل شما ارسال گردید'

    def form_valid(self, registerForm):
        # user = registerForm.save(commit=False)
        # user.is_active = False
        # user.save()
        subject = 'سایت من'
        message = 'ثبت نام شما در سایت با موفقیت صورت گرفت'
        from_email = settings.EMAIL_HOST_USER
        recipient = registerForm.cleaned_data.get('email')
        send_mail(subject,message, from_email, [recipient], fail_silently=False)
        messages.success(self.request , '! تمام شد !')
        return super().form_valid(registerForm)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


class loginview (LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my'] = My.objects.all()
        context['menusite'] = Category.objects.all()
        context['footer'] = My.objects.all()
        context['slider'] = Slider.objects.all()
        context['post'] = Post.objects.all()
        return context


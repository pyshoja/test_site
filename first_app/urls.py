from django.urls import path

from first_app.views import firstpageview , registerview , aboutview , description , filter , loginview , testview


urlpatterns = [
    path('profile/',firstpageview.as_view(), name='firstpage'),
    path('accounts/', registerview.as_view(), name='register'),
    path('login/', loginview.as_view(), name='login'),
    path('about/', aboutview.as_view(), name='about'),
    path('description/<slug:slug>/', description.as_view(), name='description'),
    path('filter/<int:category_id>/', filter.as_view() , name= 'filter'),
    path('test/', testview.as_view(), name='test'),
]
from django.urls import path

from first_app.views import firstpageview , registerview , aboutview , description , filter_category , loginview , filter_author


urlpatterns = [
    path('',firstpageview.as_view(), name='firstpage'),
    path('singup/', registerview.as_view(), name='register'),
    path('login/', loginview.as_view(), name='loginsite'),
    path('about/', aboutview.as_view(), name='about'),
    path('description/<slug:slug>/', description.as_view(), name='description'),
    path('filter/<int:category_id>/', filter_category.as_view() , name= 'filter'),
    path('author/<int:author_id>/', filter_author.as_view(), name='author'),

]
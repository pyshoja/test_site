from django.contrib.auth import views
from django.urls import path
from first_app.views import PasswordResetView , PasswordResetDoneView , PasswordResetCompleteView
from account.views import (
                    homeadmin ,
                    postlist ,
                    postcreate ,
                    postupdate ,
                    postdelete ,
                    categorylist ,
                    categorycreate ,
                    categoryupdate ,
                    categorydelete ,
                    profile ,
                    mycreate ,
                    mylist ,
                    myupdate ,
                    mydelete ,
                    sliderlist ,
                    slidercreate ,
                    sliderupdate ,
                    sliderdelete ,
                    supportlist ,
                    supportcreate ,
                    supportupdate ,
                    supportdelete ,
                    commentlist ,
                    commentupdate ,
                    commentdelete ,

)


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]



urlpatterns += [
    path('homeadmin/', homeadmin.as_view(), name='homeadmin'),

    path('postlist/', postlist.as_view(), name='postlist'),
    path('postcreate/', postcreate.as_view(), name='postcreate'),
    path('postupdate/<int:pk>/', postupdate.as_view(), name='postupdate'),
    path('postdelete/<int:pk>/', postdelete.as_view(), name='postdelete'),

    path('categorylist/', categorylist.as_view(), name='categorylist'),
    path('categorycreate/', categorycreate.as_view(), name='categorycreate'),
    path('categoryupdate/<int:pk>/', categoryupdate.as_view(), name='categoryupdate'),
    path('categorydelete/<int:pk>/', categorydelete.as_view(), name='categorydelete'),

    path('profile/', profile.as_view(), name='profile'),

    path('mylist/', mylist.as_view(), name='mylist'),
    path('mycreate/', mycreate.as_view(), name='mycreate'),
    path('myupdate/<int:pk>/', myupdate.as_view(), name='myupdate'),
    path('mydelete/<int:pk>/', mydelete.as_view(), name='mydelete'),

    path('sliderlist/', sliderlist.as_view(), name='sliderlist'),
    path('slidercreate/', slidercreate.as_view(), name='slidercreate'),
    path('sliderupdate/<int:pk>/', sliderupdate.as_view(), name='sliderupdate'),
    path('sliderdelete/<int:pk>/', sliderdelete.as_view(), name='sliderdelete'),

    path('supportlist/', supportlist.as_view(), name='supportlist'),
    path('supportcreate/', supportcreate.as_view(), name='supportcreate'),
    path('supportupdate/<int:pk>/', supportupdate.as_view(), name='supportupdate'),
    path('supportdelete/<int:pk>/', supportdelete.as_view(), name='supportdelete'),

    path('commentlist/', commentlist.as_view(), name='commentlist'),
    path('commentupdate/<int:pk>/', commentupdate.as_view(), name='commentupdate'),
    path('commentdelete/<int:pk>/', commentdelete.as_view(), name='commentdelete'),

]
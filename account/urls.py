from django.contrib.auth import views
from django.urls import path
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
                    )


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    #
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
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

]
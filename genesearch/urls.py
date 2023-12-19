from django.urls import path, include
from genesearch import views
from genesearch.views import ExceldataViewset
from rest_framework import routers

from django.contrib import admin
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register(r'exceldatas', ExceldataViewset)

urlpatterns = [
    path('', views.home),
    # path('login/', views.login),
    path('loginIN/', views.loginIN),
    # path('search/', views.search),
    path('searchnew/', views.searchnew),
    # path('search_results/', views.search_results, name='search_results'),
    # path('searchapi/', views.my_view),
    path('Apihome/', views.Apihome),
    path('', include(router.urls)),
    # path('searchapi/', views.search_by_gene),
    path('searchapi/', views.search_by_gene),
    path('searchdatabase/', views.search_by_geneDB),

    path('register/' ,register_attempt),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    # path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    # path('password_reset_request/', password_reset_request),
    # path('password_reset_verify/', password_reset_verify),
    # path('password_reset_request/', password_reset_request, name='password_reset_request'),
    path('reset_password/', views.send_reset_email, name='send_reset_email'),
    path('reset_password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password_link'),
    path('mainadmin/',adminpage),


]

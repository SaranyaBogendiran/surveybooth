from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
path('', views.index, name='index'),
path('login/', views.login_view, name='login'),
path('register/', views.register, name='register'),
path('dashboard/', views.dashboard, name='dashboard'),
path('', views.logout_view, name='logout'),
path('passwordreset/', views.password_change, name='password_change'),
path('passwordreset/email/', views.passwordreset_mail, name='passwordreset_mail'),
url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
url(r'passwordreset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.passwordreset, name='passwordreset'),
path('email/', views.emailView, name='email'),
path('success/', views.successView, name='success'),
url(r'^ajax/validate_registerform/$', views.validate_registerform, name='validate_registerform'),
url(r'^ajax/login_validation/$', views.login_validation, name='login_validation'),
]

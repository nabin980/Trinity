from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register-login/', views.register_login, name='register_login'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset-password'),
    path('admin-verify/', views.admin_verify, name='admin-verify'),
 ]
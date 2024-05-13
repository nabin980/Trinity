from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('list_users/', views.list_users, name ='list_users' ),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('user_experiences/', views.user_experiences, name='user_experiences'),
    path('delete_user_experience/<int:user_experience_id>/', views.delete_user_experience, name='delete_user_experience'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('quotation_request/', views.quotation_request, name='quotation_request'),
    path('delete_quotation_request/<int:quotation_request_id>/', views.delete_quotation_request, 
         name='delete_quotation_request'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('send_email/<int:quotation_request_id>/', views.send_email, name='send_email'),
    path('share_your_experience/', views.share_user_experience, name='share_experience'),
    path('publish_testimonials/', views.publish_testimonials, name='publish_testimonials'),  
 ]
"""
URL configuration for tms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from e_admin import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home),
    path("Home",views.Home),
    path("Donation",views.Donation,name="donation"),    
    path("Information",views.Information),
    path("Festival_Gallery",views.Festival_Gallery),
    path("Photo_Gallery",views.Photo_Gallery),
    path("Store",views.Store),
    path("scienceAndReligions1",views.scienceAndReligions1),
    path("scienceAndReligions2",views.scienceAndReligions2),
    path("scienceAndReligions3",views.scienceAndReligions3),
    path("scienceAndReligions4",views.scienceAndReligions4),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignIn",views.handleLogin,name="SignIn"),
    path("logout",views.handleLogout , name="handlelogout"),
    path("Schedule",views.Schedule),
    path("Room_Booking",views.Room_Booking,name="room_booking"),
    path("Profile",views.Profile),
    path("News_And_Event",views.News_And_Event),
    path("Feedback",views.Feedback,name="feedback"), 
    # path("saveEnquiry",views.saveEnquiry,name="saveenquiry"), 
    path("Verification_otp",views.Verification_otp,name="Verification_otp"),
    path('Profile' , views.Profile , name='Profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

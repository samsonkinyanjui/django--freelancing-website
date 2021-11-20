from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import Settings




urlpatterns = [
    path('',views.Homepage,name='Homepage.html'),
    path('register',views.register,name='register.html'),
    path('register/<str:i_number>',views.register,name='register.html'),
    path("Home", views.Home, name="Home.html"),
    path('login',views.login,name='login.html'),
    path('Dashboard',views.Dashboard,name='Dashboard.html'),
    path('Bid',views.Bid,name='Bid.html'),
    path('privacy',views.privacy,name='privacy.html'),
    path('Home2',views.Home2,name='home2.html'),
    path('Payment',views.Payment,name='Payment.html'),
    path('completedbids',views.completedbids,name='completedbids.html'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
    path('Profile2',views.Profile2,name='Profile2.html'),
    path('withd',views.withd,name='withd.html'),


]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('profile',views.profile,name="profile"),
    path('logout',views.logout,name="logout"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('change-password/', views.change_password, name='change_password'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='forgot_password'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
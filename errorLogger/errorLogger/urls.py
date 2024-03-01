from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('', include('log.urls')),
    path('accounts/', include('allauth.urls')),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='users/password_reset_email.html'), name='reset_password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='users/password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset.html'), name='password_reset_confirm'),
    path('reset-password-success', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_success.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

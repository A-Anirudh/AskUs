from django.urls import path, include
from users import views as user_views
from .views import SignUpView, ProfileUpdateView
from django.urls import reverse_lazy

urlpatterns = [
    path('profile/<str:username>', user_views.profile, name='profile'),
    path('profile/<str:username>/update', ProfileUpdateView.as_view(), name='profile-update'),
    path('register/', SignUpView.as_view(), name='register'),    
    path('login/', user_views.login, name='login'),
    path('logout/', user_views.logout, name='logout'),
    # path('captcha/', include('captcha.urls')),

]
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.AppUserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', include([
        path('', views.profile_details, name='profile-details'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        # path('delete/', views.profile_delete, name='profile-delete')
    ]))
]
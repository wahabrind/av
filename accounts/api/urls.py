
from django.urls import path,include
from . import views
urlpatterns = [
    path('request-reset-email/', views.RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/',views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
]

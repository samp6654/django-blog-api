from django.urls import path
from .views import ForgotPasswordView, RegisterView, LogoutView, LoginView, ResetPasswordView
from .views import PromoteUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('admin/promote-user/', PromoteUserView.as_view(), name='promote-user'),

    # forgot password
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),

]

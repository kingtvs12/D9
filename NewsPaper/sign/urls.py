from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import upgrade_account

urlpatterns = [
    path('upgrade/', upgrade_account, name='sign_upgrade')

    # switched to allauth
    #
    # path('login/',
    #     LoginView.as_view(
    #         authentication_form=CustomLoginForm,
    #         template_name='sign/login.html'),
    #     name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('signup/',
    #     BaseRegisterView.as_view(
    #         template_name='sign/signup.html'),
    #     name='signup'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("login_ok/", views.login_ok, name="login_ok"),
    path("signup_success/", views.signup_success, name="signup_success"),
]

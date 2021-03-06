from django.urls import path, re_path

from . import views

app_name="accounts"

urlpatterns = [
    path('login/',views.login_view, name='loginurl'),
    path('signup/', views.signup_view, name='signupurl'),
    path('logout/', views.logout_view, name='logouturl'),
]

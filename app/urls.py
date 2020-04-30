from django.urls import path,include
from . import views
urlpatterns = [
    
    path("",views.IndexPage,name="index"),
    path("register/",views.RegisterUser,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("login/",views.LoginUser,name="login"),
    path("logout/",views.logout,name="logout"),
    path("home/",views.homepage,name="home"),
    path("js/",views.JSPage,name="js")
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path(route="register/",         view=RegisterView.as_view(),        name="register"),
    path(route="login/",            view=TokenObtainPairView.as_view(), name="login"),
    path(route="token/refresh/",    view=TokenRefreshView.as_view(),    name="token_refresh"),
    path(route="profile/",          view=ProfileView.as_view(),         name="profile"),
]
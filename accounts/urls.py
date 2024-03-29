from django.urls import path
from .views import SignUpView, SecretPageView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('secret/', SecretPageView.as_view(), name='secret_page'),
]

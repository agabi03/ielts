from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

    def form_invalid(self, form):
        # Возвращаем форму с ошибками валидации
        return super().form_invalid(form)


class SecretPageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/secret_page.html'

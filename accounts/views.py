from django.urls import reverse_lazy
from django.views import generic
from .forms import MemberCreationForm


class SignUp(generic.CreateView):
    form_class = MemberCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

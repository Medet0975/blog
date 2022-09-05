from django.views import generic
from django.contrib.auth import get_user_model
from django.urls import reverse



User = get_user_model()


# Create your views here.html
class UserCreateView(generic.CreateView):
    template_name = 'registration/register.html'
    model = User


    def get_success_url(self):
        return reverse("login")
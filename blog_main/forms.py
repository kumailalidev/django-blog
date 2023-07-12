from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    Extending functionality of default user creation form
    """

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

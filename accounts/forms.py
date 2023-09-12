from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    docstring
    """

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ("username", "email", "age")


class CustomUserChangeForm(UserChangeForm):
    """
    docstring
    """

    class Meta:
        """
        docstring
        """

        model = CustomUser
        fields = ("username", "email", "age")

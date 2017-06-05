from django.contrib.auth import get_user_model #retunr user models that is active in this project
from django.contrib.auth.forms import UserCreationForm #built in creation form
#https://docs.djangoproject.com/en/1.11/topics/auth/default/

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name" #custom label for username field
        self.fields["email"].label = "Email address"
        self.fields["password2"].label = "Confirm Password"


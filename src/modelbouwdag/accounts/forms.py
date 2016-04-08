from django.contrib.auth.forms import UserCreationForm as _UserCreationForm

from .models import User


class UserCreationForm(_UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)

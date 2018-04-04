from django.contrib.auth.forms import UserCreationForm
from .models import User
from sympy.polys.fields import field

class RegisterForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        
        model = User
        fields = ("username", "email")
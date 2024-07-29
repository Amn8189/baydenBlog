from blogApp.models import Author
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class AuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Author
        fields = UserCreationForm.Meta.fields + ("age", "name")
        
class AuthorChangeForm(UserChangeForm):
    class Meta:
        model = Author
        fields = UserCreationForm.Meta.fields # First name, second name etc
        
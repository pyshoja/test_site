from django import forms
from account.models import User

class profileform (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(profileform, self).__init__(*args,**kwargs)

        self.fields['username'].help_text = None
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['is_author'].disabled = True
            self.fields['special_user'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_author', 'special_user', 'image']

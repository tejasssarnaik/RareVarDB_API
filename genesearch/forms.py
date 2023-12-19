from django import forms

class APIURLForm(forms.Form):
    api_url = forms.URLField(label='API URL', max_length=200, required=True)


from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField()
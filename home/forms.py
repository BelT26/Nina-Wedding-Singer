from django import forms


class ContactForm(forms.Form):
    """
    A form for users to contact Nina
    """
    name = forms.CharField(max_length=150)    
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=3000)

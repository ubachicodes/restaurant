from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    from_email = forms.EmailField(required = True)
    message = forms.CharField(widget=forms.Textarea, required=True)
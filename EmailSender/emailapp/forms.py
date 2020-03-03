from django import forms

class Subscribe(forms.Form):
    Name = forms.CharField(help_text="contact us")
    Description  = forms.CharField()
    Email = forms.EmailField()

    def __str__(self):
        return self.Email

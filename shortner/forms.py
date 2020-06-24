from django import forms

class URLForm(forms.Form):
    targetURL = forms.CharField(label="Target Url", max_length=100)
    hash = forms.CharField(label="Hash", max_length=15, required=False)
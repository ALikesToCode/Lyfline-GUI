from django import forms

class MammogramForm(forms.Form):
    file = forms.FileField()

class HistopathologyForm(forms.Form):
    file = forms.FileField()

class UltrasoundForm(forms.Form):
    file = forms.FileField()
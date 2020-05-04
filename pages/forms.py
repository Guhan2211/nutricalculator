from django import forms

class CallMet(forms.Form):
    txt = forms.CharField(max_length=500,
    label="",
    required=True,
    widget=forms.Textarea(
        attrs={
            "id":"id_txt",
            "placeholder":'2kg chicken,2 spoon oil'
        }
    )
    )
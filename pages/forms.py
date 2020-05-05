from django import forms

class CallMet(forms.Form):
    txt = forms.CharField(max_length=500,
    label="",
    required=True,
    widget=forms.Textarea(
        attrs={
            "cols":40,
            "id":"id_txt",
            "placeholder":'2kg chicken,2 spoon oil'
        }
    )
    )
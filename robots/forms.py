from django import forms


class RobotCreateForm(forms.Form):
    model = forms.CharField(max_length=50)
    version = forms.CharField(max_length=50)
    created = forms.DateTimeField()

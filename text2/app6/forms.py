from django import forms
class employeeform(forms.Form):
    eid = forms.IntegerField()
    name =  forms.CharField(max_length=30)
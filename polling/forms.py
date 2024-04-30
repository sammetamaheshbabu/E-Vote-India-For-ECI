from django import forms


class PollingForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    epic_number = forms.CharField(max_length=100)
    polling_station_number = forms.CharField(max_length=5)
    aadhaar_number = forms.CharField(max_length=12)
    mobile_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    captured_image = forms.ImageField()


class VoteForm(forms.Form):
    epic_number = forms.CharField(max_length=100, widget=forms.HiddenInput)
    vote = forms.CharField(max_length=100)

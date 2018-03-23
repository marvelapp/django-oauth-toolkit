from django import forms


class AllowForm(forms.Form):
    allow = forms.BooleanField(required=False)
    redirect_uri = forms.CharField(widget=forms.HiddenInput())
    scope = forms.CharField(widget=forms.HiddenInput())
    client_id = forms.CharField(widget=forms.HiddenInput())
    state = forms.CharField(required=False, widget=forms.HiddenInput())
    response_type = forms.CharField(widget=forms.HiddenInput())
    code_challenge = forms.ChoiceField(required=False, widget=forms.HiddenInput(), choices=(('S256', 'S256')))
    code_challenge_method = forms.CharField(required=False, widget=forms.HiddenInput())

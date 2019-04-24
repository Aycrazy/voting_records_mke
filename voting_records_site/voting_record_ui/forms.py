from django import forms


class UserInput(forms.Form):
    alder = forms.CharField(help_text="Enter a Alderman Name")

    def upper_name(self):
        return self.alder.upper()

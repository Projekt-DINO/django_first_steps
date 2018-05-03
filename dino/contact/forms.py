# make sure this is at the top if it isn't already
from django import forms


# With the CSS class 'form-control' you give the form a bootstrap design since bootstrap is integrated into the project.
# From now on the contact form looks nice and professional
class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    contact_name.widget.attrs.update({'placeholder': 'Your Name'})

    contact_email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    contact_email.widget.attrs.update({'placeholder': 'Your E-Mail'})

    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )
    content.widget.attrs.update({'placeholder': 'Your Message'})

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = ""
        self.fields['contact_name'].placeholder = ""
        self.fields['contact_email'].label = ""
        self.fields['content'].label = ""

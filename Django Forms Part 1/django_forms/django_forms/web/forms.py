from django import forms


class PersonForm(forms.Form):
    GENDERS = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )

    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name',
        widget=forms.TextInput(
            # This corresponds to 'HTML attributes'
            attrs={
                'placeholder': 'Enter your name',
                'class': 'form-control'
            },
        )
    )

    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text='Enter your age',
        # Default for 'IntegerField'
        widget=forms.NumberInput()
    )

    story = forms.CharField(
        widget=forms.Textarea(),
    )

    email = forms.CharField(
        widget=forms.EmailInput(),
    )

    url = forms.CharField(
        widget=forms.URLInput (),
    )

    secret = forms.CharField(
        widget=forms.PasswordInput(),
    )

    gender = forms.ChoiceField(
        # 'widget=forms.Select' is default for 'ChoiceFiled'
        choices=GENDERS,
        widget=forms.RadioSelect,
    )

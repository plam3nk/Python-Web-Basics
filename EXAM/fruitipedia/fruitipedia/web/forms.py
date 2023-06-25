from django import forms

from fruitipedia.web.models import Profile, Fruit


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'password')

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Password',
                    'data-toggle': 'password'
                }
            ),
        }


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url', 'age')

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Fruit.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name',
                }
            ),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description',
                }
            ),

            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }


class FruitEditForm(FruitCreateForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description', 'nutrition')

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }


class FruitDeleteForm(FruitCreateForm):
    class Meta:
        model = Fruit
        fields = ('name', 'image_url', 'description',)

        labels = {
            'name': 'Name',
            'image_url': 'Image URL',
            'description': 'Description',
            'nutrition': 'Nutrition',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
            field.required = False

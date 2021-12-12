from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class NewUSerForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50'}),label= 'Usuario',required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control w-50'}),label ='Correo electronico',required=True)
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50'}),label ='Numero de telefono',required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50'}),label='Nombre completo',required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50'}),label='Apellido',required=True)
    password1 = forms.CharField(label=('Contraseña'),widget=(forms.PasswordInput(attrs={'class':'form-control w-50'})),required=True)
    password2 = forms.CharField(label=('Confirmar Contraseña'),widget=(forms.PasswordInput(attrs={'class':'form-control w-50'})),required=True)
    


    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2")
        help_texts = {k:"" for k in fields }
       

    def save(self,commit=True):
        user = super(NewUSerForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        

        if commit:
            user.save()
        return user
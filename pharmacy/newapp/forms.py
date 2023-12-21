from django import forms
from .models import user,Product

class PharmaEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['UserName','Email','Address','PhoneNo','Password']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['UserName','Email','Address','PhoneNo','Password']

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Image','MedicineName','Price']


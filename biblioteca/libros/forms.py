
from django import forms

from .models import Libro

class LibroModelForm(forms.ModelForm):
    Nombre = forms.CharField(label='',
                                widget=forms.Textarea(
                                          attrs={'rows':'1','placeholder':"Nombre del libro",
                                                 'class': "textarea"}
                                ))
    Autor = forms.CharField(label='',
                                widget=forms.Textarea(
                                          attrs={'rows':'1','placeholder':"Autor del libro",
                                                 'class': "textarea"}
                                ))
    Editorial = forms.CharField(label='',
                                widget=forms.Textarea(
                                          attrs={'rows':'1','placeholder':"Editorial del libro",
                                                 'class': "textarea"}
                                ))
    ISBN = forms.CharField(label='',
                                widget=forms.Textarea(
                                          attrs={'rows':'1','placeholder':"ISBN del libro",
                                                 'class': "textarea"}
                                ))
    precio =forms.IntegerField(label='',
                                widget=forms.Textarea(
                                          attrs={'rows':'1','placeholder':"Precio del libro",
                                                 'class': "textarea"}
                                ))

    class Meta:
        model = Libro
        fields = [
            # "user",
            "Nombre",
            "Autor",
            "Editorial",
            "ISBN",
            "precio"
            ]

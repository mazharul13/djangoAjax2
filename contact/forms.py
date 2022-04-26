from django import forms
from django.forms import DateTimeField

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        # widgets = {'ename': forms.DateInput}
        help_texts = {
            'ename': ('Some useful help text.'),
            'eemail': ('Some useful help text333.'),
        }
        # CHOICES = [('1', 'First'), ('2', 'Second')]
        # choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

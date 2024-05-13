from django import forms
from .models import QuotationRequest, UserExperience

class QuotationRequestForm(forms.ModelForm):
    class Meta:
        model = QuotationRequest
        fields = ['name', 'email', 'contact_number', 'quotation_request']

    def clean_contact_number(self):
        contact_number = self.cleaned_data['contact_number']
        
        if len(contact_number) != 10:
            raise forms.ValidationError('Contact number must be 10 digits long.')

        return contact_number

class UserExperienceForm(forms.ModelForm):
    class Meta:
        model = UserExperience
        fields = ['fullname', 'rating', 'comment', 'picture']

from .models import Comment, BookAParty
from django import forms


class CommentForm(forms.ModelForm):
    """
    Create a form to make comments
    """
    class Meta:
        model = Comment
        fields = ('body',)


class BookingForm(forms.ModelForm):
    """
    Create a form to book a party
    """
    class Meta:
        model = BookAParty
        fields = ('party_theme', 'balloons', 'bouncy_castle', 'kids_age',
                  'number_of_teepees', 'street', 'city', 'county', 'eircode',
                  'date', 'email', 'phone_number', 'additional_info',)

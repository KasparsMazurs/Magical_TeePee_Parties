from .models import Comment, BookAParty
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookAParty
        fields = ('party_theme', 'balloons', 'bouncy_castle', 'kids_age', 'number_of_teepees', 'street', 'city', 'county', 'eircode', 'date', )
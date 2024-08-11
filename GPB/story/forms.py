from django import forms
from .models import UserStory

class UserStoryForm(forms.ModelForm):
    class Meta:
        model = UserStory
        fields = ['personality_type', 'story']


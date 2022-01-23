from django import forms
from app.models import Rating
from app.config import config as c

class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
    rate = forms.ChoiceField(choices=c.RATE_CHOICES, widget=forms.Select(), required=True)

    class Meta:
        model = Rating
        fields = ('text', 'rate')


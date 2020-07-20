from django import forms
from .models import Ads

class AdsForm(forms.ModelForm):

    class Meta:
        model = Ads
        fields = ['category','adname','description','ad_image','ad_image_two']
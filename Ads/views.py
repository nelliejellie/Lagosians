from django.shortcuts import render, get_object_or_404
from .models import Ads
from django.contrib.auth.decorators import login_required
from .prices import weekly_price, monthly_price, yearly_price

# Create your views here.
@login_required
def ad_view(request):
    ad = Ads.objects.all()
    return render(request, 'ads/home.html')


@login_required
def pricing_view(request):
    ad = Ads.objects.all()
    context = {
        'weekly_price': weekly_price,
        'monthly_price': monthly_price,
        'yearly_price': yearly_price,
        'ad': ad,
    }
    return render(request, 'ads/pricing-plan.html', context)
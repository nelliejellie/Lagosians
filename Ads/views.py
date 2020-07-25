from django.shortcuts import render, get_object_or_404, redirect
from .models import Ads
from django.contrib.auth.decorators import login_required
from .prices import weekly_price, monthly_price, yearly_price
from .forms import AdsForm
from datetime import datetime
import datetime as dt
from django.utils import timezone
from .tasks import delete_daily_ads,print_val, daily_ad_posted

# Create your views here.
@login_required
def ad_view(request):
    ad = Ads.objects.all()
    return render(request, 'ads/home.html')


@login_required
def pricing_view(request):
    ad = Ads.objects.all()
    for people in ad:
        if (people.user == request.user):
            print (people.weekly_ad)
    delete_daily_ads()
    context = {
        'weekly_price': weekly_price,
        'monthly_price': monthly_price,
        'yearly_price': yearly_price,
        'ad': ad,
    }
    return render(request, 'ads/pricing-plan.html', context)

@login_required
def ad_form(request):
    if request.method == 'POST':
        form = AdsForm(data=request.POST or None, files=request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_ad = form.save(commit=False)
            #new_ad.slug = new_ad.adname
            new_ad.user = request.user
            new_ad.daily_ad = True
            new_ad.expiry_date = datetime.now().date() + dt.timedelta(days=1)
            new_ad.save()
            daily_ad_posted(new_ad.id)
            return redirect(new_ad.get_absolute_url())
    else:
        #build form with data provided by the bookmarklet via get
        form = AdsForm()

    context = {
        'form' : form
    }
    return render(request, 'ads/ad_form.html', context)

def ad_detail(request, id, slug):
    ad = get_object_or_404(Ads, id=id, slug=slug)
    context = {
        'ad' : ad,
    }
    return render(request, 'ads/details.html', context)

    
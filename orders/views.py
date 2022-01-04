import stripe
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


# Create your views here.
class OrderPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=3900,
            currency = 'usd',
            description = 'Purchase Book',
            source = request.POST['stripeToken']
        )

    return render(request, 'orders/charges.html')
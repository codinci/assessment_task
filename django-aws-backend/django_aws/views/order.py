from django.shortcuts import render, redirect
from ..models import Order
from django.conf import settings
import africastalking
from django.utils import timezone
import requests


# Initialize Africa's Talking SDK
africastalking.initialize(
    username=settings.AFRICAS_TALKING_USERNAME,
    api_key=settings.AFRICAS_TALKING_API_KEY
)

sms = africastalking.SMS


def place_order(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        # Get product from form or default
        product_name = request.POST.get('product_name', 'Unknown Product')
        user = request.user

        # Create an order with the current user and product details
        order = Order.objects.create(
            user=user,
            product_name=product_name,
            order_time=timezone.now()
        )

        # Send SMS via Africa's Talking
        try:
            url = 'https://api.africastalking.com/version1/messaging'
            headers = {
                            'ApiKey': settings.AFRICAS_TALKING_API_KEY,
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept': 'application/json'
                        }
            body = {
                        'username': settings.AFRICAS_TALKING_USERNAME,
                        'from': 17145,
                        'message':  "Thank you for making an order with us.",
                        'to': phone_number
                    }
            response = requests.post(url=url, headers=headers, data=body)
            data = response.json().get('SMSMessageData').get('Recipients')[0]
            print('Hello')
            print(data)
        except Exception as e:
            print(f"Failed to send SMS: {e}")

        return redirect('home')
    return redirect('home')

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
        sender = '8576' #Place a valid sender id
        # Send SMS via Africa's Talking
        try:
            message = f"Hello {user.username}, thank you for your order of {product_name}. We will notify you once it's ready!"
            response = sms.send(message, [phone_number], sender)
            print("SMS Response: ", response)
        except Exception as e:
            print(f"Failed to send SMS: {e}")

        return redirect('home')
    return redirect('home')

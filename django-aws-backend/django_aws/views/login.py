from django.shortcuts import render
from .auth_provider import AuthProvider

auth_provider = AuthProvider()


def login(request):
    authorization_url = auth_provider.get_authorization_url()
    return redirect(authorization_url)


def callback(request):
    auth_data = auth_provider.authenticate(request)

    # Access the authentication data
    access_token = auth_data['access_token']
    expires = auth_data['expires']
    refresh_token = auth_data['refresh_token']
    resource_owner = auth_data['resource_owner']

    # Use the authentication data as needed
    return render(request, 'callback.html', {
        'access_token': access_token,
        'expires': expires,
        'refresh_token': refresh_token,
        'resource_owner': resource_owner})

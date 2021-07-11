from django.urls import path

from authentication.views import CreateUserView, TokenAuthenticathionView

app_name = 'authentication'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token', TokenAuthenticathionView.as_view(), name='token'),
]
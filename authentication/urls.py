from django.urls import path

from authentication.views import CreateUserView, ObtainTokenView

app_name = 'auth'

urlpatterns = [
    path('auth/registration/', CreateUserView.as_view(), name='registration'),
    path('auth/token/', ObtainTokenView.as_view(), name='token'),
]

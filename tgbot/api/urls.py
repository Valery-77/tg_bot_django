from django.urls import path
# from rest_framework import routers
from .views import BotUsersAPIView, BotHelpAPIView

# router = routers.SimpleRouter()
# router.register(r'bot-user', BotUsersAPIView)

urlpatterns = [
    path('bot-user/', BotUsersAPIView.as_view(), name='bot-user'),
    path('bothelp-user/', BotHelpAPIView.as_view(), name='bothelp-user')
    # path('', include(router.urls))
]

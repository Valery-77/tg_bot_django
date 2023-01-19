from django.urls import path
# from rest_framework import routers
from .views import BotUsersAPIView

# router = routers.SimpleRouter()
# router.register(r'bot-user', BotUsersAPIView)

urlpatterns = [
    path('bot-user', BotUsersAPIView.as_view(), name='bot-user')
    # path('', include(router.urls))
]

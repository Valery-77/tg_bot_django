from rest_framework.generics import ListCreateAPIView
from .models import BotUser
from .serializers import BotUserSerializer


# Create your views here.
class BotUsersAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer

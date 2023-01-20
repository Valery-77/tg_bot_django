from rest_framework.generics import ListCreateAPIView
from .models import BotUser, BotHelp
from .serializers import BotUserSerializer, BotHelpSerializer


# Create your views here.
class BotUsersAPIView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class BotHelpAPIView(ListCreateAPIView):
    queryset = BotHelp.objects.all()
    serializer_class = BotHelpSerializer

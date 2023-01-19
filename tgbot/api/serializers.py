from rest_framework import serializers
from .models import BotUser


class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = ('registration', 'channel', 'user_id', 'username', 'first_name', 'last_name', 'email', 'mobile',
                  'link', 'utm_source', 'utm_campaign', 'utm_medium', 'utm_term', 'utm_content', 'last_visit')

import enum

from rest_framework import serializers

from api_server.apps.text.models import Lang


class TokenizationOutputFormat(enum.Enum):
    WAKACHI = 'wakachi'
    ALL_INFO = 'all_info'


class TokenizationParamsSerializer(serializers.Serializer):
    """Params serializer"""
    format = serializers.ChoiceField(choices=[e.value for e in TokenizationOutputFormat])


class TokenizationSerializer(serializers.Serializer):
    """Base serializer of tokenization"""
    lang = serializers.ChoiceField(choices=[e.value for e in Lang])
    params = TokenizationParamsSerializer()


class TokenizationRequestSerializer(TokenizationSerializer):
    """Request body serializer"""
    data = serializers.CharField(max_length=1000)


class TokenizationResponseSerializer(TokenizationSerializer):
    """Response serializer"""
    result = serializers.JSONField()

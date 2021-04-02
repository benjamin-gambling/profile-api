from rest_framework import serializers


class HellosSerializers(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)

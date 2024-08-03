from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=5)
    age = serializers.IntegerField(min_value=18)
    
class StudMarksSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    marks = serializers.IntegerField(min_value=0, max_value=100)
    
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
 
class Hello(APIView):
    """TESTING APIVIEW"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        my_api_view = [
            'Uses HTTP methods as function names',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
            'similar to django view - traditional',
            'written by dev toony',
        ]
        return Response({ 'message' : my_api_view })
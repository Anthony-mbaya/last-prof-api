from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api_app import serializers
# Create your views here.
 
class Hello(APIView):
    """TESTING APIVIEW"""
    #ensures all post,patch,put request undergo serializer
    serializer_class = serializers.HelloSerializer
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
    
    def post(self, request):
        """Create a hello message with our name"""
        #retrieve serializer class
        serializer = self.serializer_class(data=request.data)
        #check if serializer is valid
        if serializer.is_valid():
            #retrive field defined in the serializer
            name = serializer.validated_data.get('name')
            age = serializer.validated_data.get('age')
            message = f'Hello dev {name} age {age}yrs'
            return Response({ 'message' : message })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method' : 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method' : 'DELETE'})
        

class StudentMarks(APIView):
    """Returns student marks"""
    serializer_class = serializers.StudMarksSerializer
    def get(self, request, format=None):
        """Returns a list of student marks"""
        student_marks = [
            {'name' : 'dev', 'marks' : 90},
            {'name' : 'tony', 'marks' : 80},
            {'name' : 'john', 'marks' : 70},
            ]
        return Response(student_marks)
    def post(self, request):
        """Create a student marks"""
        studMarksSerializer = self.serializer_class(data=request.data)
        if studMarksSerializer.is_valid():
            studName = studMarksSerializer.validated_data.get('name')
            studMarks = studMarksSerializer.validated_data.get('marks')
            return Response({ 'StudentMarks' : f'student {studName} got {studMarks}'})
        else:
            return Response(studMarksSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

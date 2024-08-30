from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api_app import serializers
from rest_framework import viewsets
from profiles_api_app import models  
#Token auth - gen ran token str wen user logs in checkin every req is auth
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters
from profiles_api_app import permissions
from rest_framework.permissions import IsAuthenticated
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
        

class HelloViewset(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',
            'by dev tonny',
        ]
        return Response({ 'message' : a_viewset })
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Welcome { name }'
            return Response({ 'message' : message })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #match get
    def retrieve(self, request, pk=None):
        """Handles getting an object by its id"""
        return Response({ 'message' : f'Hello {pk}' })
    
    #match http put
    def update(self, request, pk=None):
        """Update an object"""
        return Response({ 'message' : f'Hello {pk} updated'})
    #match patch
    def partial_update(self, request, pk=None):
        """Update part of an object"""
        return Response({ 'message' : f'Hello {pk} partial updated'})
    #match destroy
    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({ 'message' : f'Hello {pk} deleted'})
    

class UserProfileViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile"""
    serializer_class = serializers.UserProfileSerializer
    # determines functionalities of viewsets(CRUD) - CREATE, READ, UPDATE, DELETE ....
    queryset = models.UserProfile.objects.all() #RETRIEVE ALL DATA FROM DB
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfilesFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnBlog,
        IsAuthenticated
    )
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
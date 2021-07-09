from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import UserProfile
from .permissions import UserProfilePermission
from .serializers import HelloSerailzer, UserProfilerSerializer


class HelloViewSet(ViewSet):
    """
    Class to implement rest_framework's view sets.
    """
    serializer_class = HelloSerailzer

    def list(self, request):
        """
        Method to list all objects of these classes.
        Args:
            request:

        Returns:

        """
        response_dict = {
                "message" : "This is list method of view set",
                "test_api": "This is the operations supported, list, create, "
                            "update, retrieve, partial_update "
        }
        return Response(response_dict, HTTP_200_OK)

    def create(self, request):
        """
        Method to create the object.
        Args:
            request:

        Returns:

        """
        response_dict = { }
        szs = self.serializer_class(data = request.data)
        if szs.is_valid():
            name = szs.validated_data.get("name")
            response_dict["message"] = "Hey Hi {}".format(name)
            return Response(response_dict, HTTP_200_OK)
        return Response(szs.errors, HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        """
        Method to update the object by `pk`.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "Message": "This maps to HTTP put request"
        }
        return Response(response_dict, HTTP_200_OK)

    def retrieve(self, request, pk = None):
        """
        Method to update the object by `pk`.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "Message": "This maps to HTTP GET request"
        }
        return Response(response_dict, HTTP_200_OK)

    def destroy(self, request, pk = None):
        """
        Method to update the object by `pk`.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "Message": "This maps to HTTP delete request"
        }
        return Response(response_dict, HTTP_200_OK)

    def partial_update(self, request, pk = None):
        """
        Method to update the object by `pk`.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "Message": "This maps to HTTP patch request"
        }
        return Response(response_dict, HTTP_200_OK)


class HelloApiView(APIView):
    """
    Class to test django api views.
    Need to support all methods get, put, post, patch, delete.
    """
    serializer_class = HelloSerailzer

    def get(self, request, format = None):
        """
        Method to test the get request call.
        Args:
            request:
            format:

        Returns:

        """
        message = ["This is test message", "call to api"]
        response_dict = {
                "message": message, "test": "Hello world"
        }
        return Response(response_dict, status = HTTP_200_OK)

    def post(self, request):
        """
        Method to serve the post request made to the apiview.
        Args:
            request:

        Returns:

        """
        szs = self.serializer_class(data = request.data)
        if szs.is_valid():
            name = szs.validated_data.get("name", "No Name Found")
            response_dict = {
                    "name posted": 'Hey Hi {}'.format(name)
            }
            return Response(response_dict, status = HTTP_200_OK)
        else:
            return Response(szs.errors, status = HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        """
        Method to handle put request.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "message": "Details: ".format(self.__doc__)
        }
        return Response(response_dict, status = HTTP_200_OK)

    def patch(self, request, pk = None):
        """
        This method will update some details to object rather than the whole
        object
        .
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "message": "Details: ".format(self.__doc__)
        }
        return Response(response_dict, status = HTTP_200_OK)

    def delete(self, request, pk = None):
        """
        Method to delete the object based on a primary key `pk`.
        Args:
            request:
            pk:

        Returns:

        """
        response_dict = {
                "message": "Details: ".format(self.__doc__)
        }
        return Response(response_dict, status = HTTP_200_OK)


class UserProfileViewSet(ModelViewSet):
    """
    Class to handle user profiles.
    """
    serializer_class = UserProfilerSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserProfilePermission,)

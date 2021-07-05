from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import HelloSerailzer


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


# Create your views here.
def home_page(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "test.html")

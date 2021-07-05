from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """
    Class to test django api views.
    Need to support all methods get, put, post, patch, delete.
    """

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
        return Response(response_dict)


# Create your views here.
def home_page(request):
    """

    Args:
        request:

    Returns:

    """
    return render(request, "test.html")

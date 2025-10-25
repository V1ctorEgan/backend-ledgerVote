from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from django.conf import settings
from rest_framework import generics


# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully!"}, status=201)
#         return Response(serializer.errors, status=400)

class RegisterView(generics.CreateAPIView):
    serializer_class =RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data = request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializer.errors, status=400)
    

class AdminLoginView(APIView):
    def post(self, request):
        password = request.data.get("password")
        if password == settings.ADMIN_SECRET:
            return Response({"message": "Admin authenticated", "role": "admin"})
        return Response({"error": "Invalid admin password"}, status=401)
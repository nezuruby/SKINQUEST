from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import UserProfile
from .serializers import UserSerializer
# Create your views here.
class UserRegisterViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer

    def create(self, request):
        try:
            full_name = request.data.get("full_name")
            email = request.data.get("email")
            username = request.data.get("username")

            # Validate
            errors = {}
            if UserProfile.objects.filter(user__email=email).exists():
                errors["email"] = "Email is already registered"
            if UserProfile.objects.filter(user__username=username).exists():
                errors["username"] = "Username is already registered"
            if errors:
                return Response(errors, status=400)

            # Use serializer to create the user
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            return Response({"message": str(error)}, status=400)
    def __str__(self):
            return "UserRegisterViewSet"
        
class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.order_by("-id")
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        queryset = UserProfile.objects.all().order_by("role__name")
        id = self.request.query_params.get("id", None)

        if self.action == "list":
            queryset = queryset.exclude(role__name="superadmin")

        if id:
            queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset

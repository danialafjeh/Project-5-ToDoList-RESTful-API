from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Task
from django.contrib.auth.models import User
from .serializers import UserSerializer, TaskSerializer, RegisterUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class GetUsersList(APIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        queryset = User.objects.all()
        #serializer = UserSerializer(instance=queryset, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class GetUserDetails(APIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        instance = get_object_or_404(User, id=pk, username=request.user.username)
        serializer = UserSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK) 

class SearchUser(APIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, username):
        queryset = User.objects.filter(username__icontains=username)
        #serializer = UserSerializer(instance=queryset, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = UserSerializer(instance=result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class UpdateUser(APIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        instance = get_object_or_404(User, id=pk, username=request.user.username)
        serializer = UserSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def delete(self, request, pk):
        user = get_object_or_404(User, id=pk)
        if user == request.user:
            return Response({'message':'You can not delete your own admin account'}, status=status.HTTP_403_FORBIDDEN)
        elif user.is_superuser:
            return Response({'message':'You can not delete a superuser'}, status=status.HTTP_403_FORBIDDEN)
        else:
            user.delete()
            return Response({'message':'User deleted'}, status=status.HTTP_200_OK)

class RegisterUser(APIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response(
                {
                    'message':'User registered successfully',
                    'username':user.username,
                    'token':token.key
                }, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

class CheckAuthToken(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({"user":user.username}, status=status.HTTP_200_OK)
    
class GetTasksList(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Task.objects.filter(user__id=request.user.id)
        #serializer = TaskSerializer(instance=queryset, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class GetTaskDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        instance = get_object_or_404(Task, id=pk, user=request.user)
        serializer = TaskSerializer(instance=instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchTask(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, username):
        queryset = Task.objects.filter(user__username__icontains=username).order_by('-created_at')
        #serializer = TaskSerializer(instance=queryset, many=True)
        #return Response(serializer.data, status=status.HTTP_200_OK)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = TaskSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class AddTask(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response({'response':'Task added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTask(APIView):
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        instance = get_object_or_404(Task, id=pk, user=request.user)
        serializer = TaskSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'response':'Task updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTask(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        instance = get_object_or_404(Task, id=pk, user=request.user)
        instance.delete()
        return Response({'response':'Task deleted'}, status=status.HTTP_200_OK)



        
    
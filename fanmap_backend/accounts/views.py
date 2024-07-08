from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserBasicInfoSerializer, UserAdditionalInfoSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAuthenticated

class RegisterStepOne(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserBasicInfoSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            request.session['user_id'] = user.id # 세션에 사용자 ID 저장
            return Response({"message": "Step 1 completed. Proceed to step 2."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterStepTwo(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user_id = request.session.get('user_id') # 세션에서 사용자 ID 가져오기
        
        if not user_id:
            return Response({"error": "No user ID found in session. Please complete step 1 first."}, status=status.HTTP_400_BAD_REQUEST)
       
        # Step 1에서 저장한 사용자 ID로 사용자 조회
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserAdditionalInfoSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            del request.session['user_id']  # Clear user ID from session
            token, created = Token.objects.get_or_create(user=user) # 세션에서 사용자 ID 삭제
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomAuthToken(ObtainAuthToken):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        return Response({"detail": "This endpoint only accepts POST requests."})

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email})

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserAdditionalInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

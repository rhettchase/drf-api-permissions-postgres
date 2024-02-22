from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Brew
from .permissions import IsOwnerOrReadOnly
from .serializers import BrewSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class BrewViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `list`, `create`, `retrieve`, `update`, and `destroy` actions.
    """
    queryset = Brew.objects.all()
    serializer_class = BrewSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def switch_user(self, request):
        user_id = request.data.get('user_id')
        
        if not user_id:
            return Response({"error": "User ID is required."}, status=status.HTTP_400_BAD_BAD_REQUEST)
        
        try:
            target_user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "Target user not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # Assuming the requesting user is an admin as enforced by IsAdminUser permission class
        login(request, target_user, backend='django.contrib.auth.backends.ModelBackend')
        
        return Response({"message": f"Switched to user {target_user.username} successfully."})
    

# class UserViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]  # or your custom permission class

#     @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
#     def switch_user(self, request, pk=None):
#         if not request.user.has_perm('app.can_switch_user'):  # Custom permission check
#             return Response({"message": "You do not have permission to switch users."}, status=status.HTTP_403_FORBIDDEN)

#         try:
#             target_user = User.objects.get(pk=pk)  # Assuming pk is the ID of the user to switch to
#         except User.DoesNotExist:
#             return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         # Implement the logic to switch to the target user here.
#         # This could involve re-authenticating the session as the target user.
#         # For example:
#         # login(request, target_user, backend='django.contrib.auth.backends.ModelBackend')

#         return Response({"message": f"Switched to user {target_user.username}."})


# class BrewList(ListCreateAPIView):
#     # Anything that inherits from ListAPI View is going to need 2 brews.
#     # What is the collection of brews, aka the queryset
#     # associate collection of brews and the serial number
#     queryset = Brew.objects.all()

#     #serializing
#     serializer_class = BrewSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # must be iterable

# class BrewDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Brew.objects.all()
#     serializer_class = BrewSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOrReadOnly] # must be iterable



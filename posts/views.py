from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    # Ordenamos por '-created_datetime' para o post novo aparecer no topo do feed
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

    # Mensagem personalizada ao CRIAR um post
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                "message": "Post published successfully! 🚀",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Validation Error. Please check your data.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Mensagem personalizada ao EDITAR (Update parcial)
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response({
            "message": "Post updated successfully! ✨",
            "data": response.data
        }, status=status.HTTP_200_OK)

    # Mensagem personalizada ao DELETAR
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "The post has been deleted forever. 🗑️"
        }, status=status.HTTP_200_OK) 
        # Nota: Usamos 200 em vez de 204 para que o corpo da mensagem apareça no JSON
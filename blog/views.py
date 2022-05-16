from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, get_object_or_404, ListCreateAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post
from blog.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from blog.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class PostApiList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PostApiUpdate(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    pagination_class = PostAPIListPagination


class PostApiDestroy(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminOrReadOnly,)

# class PostApiView(ListAPIView):
#         queryset = Post.objects.all()
#         serializer_class = PostSerializer

# class PostViewSet(ModelViewSet):
#     # queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Post.objects.all()[:3]
#
#         return Post.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=False)
#     def post(self, request):
#         post = Post.objects.all()
#         return Response({'posts': [p.title for p in post]})

# class PostApiList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostApiUpdate(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostApiDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostApiView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({'posts': PostSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         post = get_object_or_404(Post.objects.all(), pk=pk)
#         post.delete()
#         return Response({"post": "Delete post " + str(pk)})

from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from blog.views import PostApiList, PostApiUpdate, PostApiDestroy
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'post', PostViewSet, basename='post')
# print(router.urls)

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/post/', PostApiList.as_view()),
    path('api/v1/post/<int:pk>/', PostApiUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>/', PostApiDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('api/v1/', include(router.urls)),
    # path('api/v1/postlist/', PostViewSet.as_view({'get': 'list'})),
    # path('api/v1/postlist/<int:pk>/', PostViewSet.as_view({'put': 'update'})),

]

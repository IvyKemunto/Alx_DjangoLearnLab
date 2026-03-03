"""
URL configuration for social_media_api project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):
    """API Root view with available endpoints."""
    permission_classes = []

    def get(self, request):
        return Response({
            'message': 'Welcome to the Social Media API',
            'version': 'v1',
            'endpoints': {
                'accounts': {
                    'register': '/api/accounts/register/',
                    'login': '/api/accounts/login/',
                    'profile': '/api/accounts/profile/',
                    'users': '/api/accounts/users/',
                    'follow': '/api/accounts/follow/<user_id>/',
                    'unfollow': '/api/accounts/unfollow/<user_id>/',
                },
                'posts': {
                    'list': '/api/posts/',
                    'detail': '/api/posts/<id>/',
                    'like': '/api/posts/<id>/like/',
                    'unlike': '/api/posts/<id>/unlike/',
                    'comments': '/api/posts/<id>/comments/',
                },
                'feed': '/api/feed/',
                'notifications': '/api/notifications/',
            }
        })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', APIRootView.as_view(), name='api-root'),
    path('api/', APIRootView.as_view(), name='api-root-alt'),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),
    path('api/notifications/', include('notifications.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

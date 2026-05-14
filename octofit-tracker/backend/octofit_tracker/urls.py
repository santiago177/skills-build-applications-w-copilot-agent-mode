from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
import os
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')

# Custom API root to show the correct Codespace URL
def custom_api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "http://localhost:8000/api/"
    return JsonResponse({
        "users": base_url + "users/",
        "teams": base_url + "teams/",
        "activities": base_url + "activities/",
        "leaderboard": base_url + "leaderboard/",
        "workouts": base_url + "workouts/"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', custom_api_root, name='api_root'),
    path('api/', include(router.urls)),
]

from django.urls import path
from .views import PostViewSet,ListPostView
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
)

from rest_framework.routers import SimpleRouter

app_name="api"
urlpatterns = [
    path('list/',ListPostView.as_view()),
    path('token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

]
router = SimpleRouter()
router.register("",PostViewSet,basename='post')
urlpatterns += router.urls

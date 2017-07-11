from django.conf.urls import url, include
from rest_framework import routers

from library import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'subjects', views.SubjectViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/', views.CreateUserView.as_view(), name='user'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

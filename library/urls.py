from django.conf.urls import url, include
from rest_framework import routers

from library import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
# router.register(r'subjects', views.SubjectViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^books/', views.BookViewSet.as_view(), name='books'),
    url(r'^register/', views.UserCreateView.as_view(), name='register'),
    url(r'^users/', views.UserListView.as_view(), name='users'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

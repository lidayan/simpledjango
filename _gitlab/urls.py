
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'namespaces', views.NamespaceViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
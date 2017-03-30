from django.conf.urls import url, include
from products import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static
from django.conf import settings


# Create a router and register our viewsets with it.



router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'news', views.NewViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

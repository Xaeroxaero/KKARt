from django.conf.urls import url, include
from news import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static
from django.conf import settings





router = DefaultRouter()
router.register(r'news', views.NewViewSet)

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from news import views as views_news
from products import views as views_products
from contact import views as views_contact
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'products', views_products.ProductViewSet)
router.register(r'users', views_products.UserViewSet)
router.register(r'news', views_news.NewViewSet)
router.register(r'contact', views_contact.ContactViewSet)

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
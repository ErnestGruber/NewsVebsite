"""
URL configuration for NewsQebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from NewsQebsite import views

from django.urls import reverse

from NewsQebsite.models import News

# Получите все экземпляры модели News
news_instances = News.objects.all()

# Создание ссылок для каждого экземпляра модели
urls = []


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path('news/<slug:url>/', views.page_view, name='newspage'),
    path('news_category/<str:category>/', views.get, name='news-list'),
]
"""

for news_instance in news_instances:
    url = reverse('news_detail', kwargs={'url': news_instance.urlEndpoint})
    urls.append(url)
    
"""

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


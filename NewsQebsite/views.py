from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta
from NewsQebsite.models import News
from NewsQebsite.settings import MEDIA_ROOT


def index(request):
    print("base dir path", MEDIA_ROOT)
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)


def news_detail(request, url):
    # Получите экземпляр модели News по полю url_endpoint
    news_instance = News.objects.get(urlEndpoint=url)

    # Создайте ссылку на отдельный URL для данного экземпляра
    news_url = reverse('news_detail', kwargs={'url': news_instance.urlEndpoint})

    # Передайте данные экземпляра в шаблон и отобразите его
    context = {'news_instance': news_instance, 'news_url': news_url}
    return render(request, 'index.html', context)  # новости детали


newsSection1 = {
    'column1_news': News.objects.order_by('-dataNews')[:2],
    'column2_news': News.objects.order_by('-dataNews')[2:5],
    'column3_news': News.objects.order_by('-dataNews')[5:9],
}
newsSections = {
    'news': News.objects.order_by('-dataNews')[9:],
}


def index(request):
    # try:

    context = {'news': newsSection1,
               'newsSections': newsSections}

    return render(request, 'index.html', context)


## except Exception as e:
##   return render(request, 'engineering_works.html')


def page_view(request, url):
    try:
        page = News.objects.get(urlEndpoint=url)
        context = {'news': page}
        return render(request, 'NewsPage.html', context)
    except News.DoesNotExist:
        return render(request, 'page_not_found.html')
    except Exception as e:
        return render(request, 'engineering_works.html')

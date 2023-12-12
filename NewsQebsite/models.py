
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name




class News(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    def upload_to(instance, filename):

        return "news_images/{filename}".format(filename=filename)


    # Fields
    urlEndpoint = models.CharField(max_length=200, help_text="url our news")
    tittleText = models.CharField(blank=True, max_length=200, help_text="Text our news")
    title = models.CharField(max_length=200, help_text="Title our news")
    titleImg = models.ImageField(blank=True, upload_to=upload_to, help_text="Title image our news")

    firstImg = models.ImageField(blank=True, upload_to=upload_to, help_text="Frst image our news")
    hoverFirst = models.CharField(blank=True, max_length=200, help_text="h1 first our news")
    firstText = models.TextField(max_length=5000, help_text="Text first our news")

    hoverSecond = models.CharField(blank=True, max_length=200, help_text="h1 second our news")
    secondText = models.TextField(blank=True, max_length=5000, help_text="Text second our news")
    secondImg = models.ImageField(blank=True, upload_to=upload_to, help_text="Second image our news")
    dataNews = models.DateTimeField(help_text="Text second our news")
    rate = models.IntegerField(serialize=True,max_length=10)
    categoryNews = models.CharField(max_length=50)
    auto_increment_id = models.AutoField(primary_key=True)
    # Metadata
    class Meta:
        ordering = ['-dataNews']

    # Methods

    def __str__(self):
        return self.tittleText

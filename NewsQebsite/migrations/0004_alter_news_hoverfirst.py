# Generated by Django 4.2.2 on 2023-06-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsQebsite', '0003_alter_news_firstimg_alter_news_hoversecond_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='hoverFirst',
            field=models.CharField(blank=True, help_text='h1 first our news', max_length=200),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsQebsite', '0004_alter_news_hoverfirst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tittleText',
            field=models.CharField(blank=True, help_text='Text our news', max_length=200),
        ),
    ]

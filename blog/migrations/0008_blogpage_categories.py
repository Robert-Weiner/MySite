# Generated by Django 2.0.7 on 2018-07-16 22:47

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]

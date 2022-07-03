# Generated by Django 4.0.5 on 2022-07-01 03:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(default='')),
                ('mainCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.category')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(default='')),
                ('featuredImage', models.ImageField(default='defaultBG.png', upload_to='uploads/images')),
                ('keywords', models.CharField(default='', max_length=400)),
                ('metaDesc', models.CharField(default='', max_length=400)),
                ('body', tinymce.models.HTMLField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(null=True)),
                ('updated', models.BooleanField(default=False)),
                ('postStatus', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='category', to='calculator.category')),
                ('subCategory', models.ManyToManyField(to='calculator.subcategory')),
            ],
        ),
    ]
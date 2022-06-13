# Generated by Django 4.0.5 on 2022-06-11 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_url', models.URLField()),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2)),
                ('site_description', models.TextField()),
                ('site_image', models.ImageField(default='default.jpg', upload_to='user_directory_path', verbose_name='Picture')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('author_profile', models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='awards.profile')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]

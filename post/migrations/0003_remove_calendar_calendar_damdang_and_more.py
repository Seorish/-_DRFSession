# Generated by Django 4.0.6 on 2022-07-23 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_todo_todocomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='calendar_damdang',
        ),
        migrations.AddField(
            model_name='calendar',
            name='calender_author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='Post_author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

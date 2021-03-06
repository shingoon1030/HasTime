# Generated by Django 3.2.12 on 2022-05-20 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='questionB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('titleQ', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionboard.questionb')),
            ],
        ),
    ]

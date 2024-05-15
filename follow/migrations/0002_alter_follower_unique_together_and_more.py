# Generated by Django 5.0.6 on 2024-05-15 12:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('user', 'follower')},
        ),
        migrations.AlterUniqueTogether(
            name='following',
            unique_together={('user', 'following')},
        ),
    ]

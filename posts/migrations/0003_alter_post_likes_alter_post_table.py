# Generated by Django 5.0.4 on 2024-04-30 04:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_alter_post_comment_ck"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name="post",
            table="posts",
        ),
    ]

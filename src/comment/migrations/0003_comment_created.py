# Generated by Django 4.2.5 on 2023-10-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0002_alter_comment_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="created",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
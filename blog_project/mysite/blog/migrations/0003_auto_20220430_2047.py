# Generated by Django 3.0 on 2022-04-30 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='activate',
            new_name='active',
        ),
    ]

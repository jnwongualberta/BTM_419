# Generated by Django 4.0.3 on 2022-03-28 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='amount_received',
        ),
    ]
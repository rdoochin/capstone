# Generated by Django 3.0.6 on 2021-04-14 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20210414_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
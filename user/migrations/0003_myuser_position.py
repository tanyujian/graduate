# Generated by Django 2.2.5 on 2020-05-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200516_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='position',
            field=models.CharField(default='学生', max_length=50),
        ),
    ]
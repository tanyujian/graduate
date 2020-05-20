# Generated by Django 2.2.5 on 2020-05-16 08:21

from django.db import migrations
import mirage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=mirage.fields.EncryptedCharField(max_length=30, verbose_name='名字'),
        ),
    ]
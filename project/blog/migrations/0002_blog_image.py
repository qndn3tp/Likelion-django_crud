# Generated by Django 4.0.4 on 2022-05-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank='True', null='True', upload_to='blog/'),
            preserve_default='True',
        ),
    ]

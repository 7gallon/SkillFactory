# Generated by Django 4.0.4 on 2022-04-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0008_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]

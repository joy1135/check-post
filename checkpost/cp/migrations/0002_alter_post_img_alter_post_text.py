# Generated by Django 5.1.6 on 2025-03-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='img_posts/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

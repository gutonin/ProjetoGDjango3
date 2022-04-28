# Generated by Django 3.2 on 2022-04-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_post_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 2.2.10 on 2021-08-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0003_auto_20210622_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

# Generated by Django 2.2.8 on 2019-12-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='summary',
            field=models.CharField(max_length=3000),
        ),
    ]

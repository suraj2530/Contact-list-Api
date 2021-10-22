# Generated by Django 3.2.7 on 2021-10-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_picture',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country_code',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]

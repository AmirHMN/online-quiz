# Generated by Django 4.0.3 on 2022-04-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_code',
            field=models.CharField(max_length=10, unique=True, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, verbose_name='شماره تلفن'),
        ),
    ]
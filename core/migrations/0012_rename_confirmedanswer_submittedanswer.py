# Generated by Django 4.0.3 on 2022-04-04 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_answer_options_alter_confirmedanswer_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConfirmedAnswer',
            new_name='SubmittedAnswer',
        ),
    ]
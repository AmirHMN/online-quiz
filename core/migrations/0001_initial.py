# Generated by Django 3.2 on 2022-04-12 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'گروه',
                'verbose_name_plural': 'گروه ها',
            },
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('won_at', models.DateField(verbose_name='برنده شده در')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل کابر',
                'verbose_name_plural': 'پروفایل های کاربران',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='متن سوال')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='core.group', verbose_name='گروه')),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوالات',
            },
        ),
        migrations.CreateModel(
            name='CorrectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('national_code', models.CharField(max_length=10, unique=True, verbose_name='کد ملی')),
                ('submitted_at', models.DateField(auto_now_add=True, verbose_name='ثبت شده در')),
                ('count', models.IntegerField(default=0)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correct_details', to='core.userprofile', verbose_name='پروفایل کاربر')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, verbose_name='متن')),
                ('correct', models.BooleanField(default=False, verbose_name='پاسخ صحیح')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='core.question', verbose_name='سوال')),
            ],
            options={
                'verbose_name': 'پاسخ',
                'verbose_name_plural': 'پاسخ ها',
            },
        ),
        migrations.CreateModel(
            name='SubmittedAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField(blank=True, verbose_name='آیدی سوال')),
                ('answer_id', models.IntegerField(verbose_name='آیدی پاسخ')),
                ('is_correct_answer', models.BooleanField(blank=True, help_text='آیا پاسخ داده شده صحیح است؟', verbose_name='پاسخ صحیح؟')),
                ('submitted_at', models.DateField(auto_now_add=True, verbose_name='ثبت شده در')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted_answers', to='core.userprofile', verbose_name='پروفایل کاربر')),
            ],
            options={
                'verbose_name': 'پاسخ ثبت شده',
                'verbose_name_plural': 'پاسخ های ثبت شده',
                'unique_together': {('user_profile', 'question_id', 'submitted_at')},
            },
        ),
    ]

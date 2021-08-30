# Generated by Django 3.2.6 on 2021-08-30 10:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0002_alter_person_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registration_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.TextField(verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(verbose_name='تاریخ تولد'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='person',
            name='entry_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ورود'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='users_images', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personal_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='person',
            name='study_field',
            field=models.CharField(max_length=300, verbose_name='رشته تحصیلی'),
        ),
    ]
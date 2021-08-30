# Generated by Django 3.2.6 on 2021-08-30 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0005_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('can_write_blog', 'Can Write Blog')]},
        ),
        migrations.AddField(
            model_name='person',
            name='register_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ثبت نام'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-24 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0003_alter_teacher_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
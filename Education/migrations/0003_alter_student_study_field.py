# Generated by Django 3.2.6 on 2021-09-07 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0002_auto_20210902_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='study_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Education.studyfield', verbose_name='رشته تحصیلی'),
        ),
    ]
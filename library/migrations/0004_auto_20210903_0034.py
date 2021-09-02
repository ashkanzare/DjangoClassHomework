# Generated by Django 3.2.6 on 2021-09-02 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0002_auto_20210902_1258'),
        ('library', '0003_alter_rent_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='study_field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.studyfield'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='library.book'),
        ),
    ]
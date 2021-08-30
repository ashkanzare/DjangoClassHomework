# Generated by Django 3.2.6 on 2021-08-30 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0004_alter_person_personal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
                ('post', models.CharField(blank=True, default=None, max_length=200, null=True, unique=True)),
            ],
            bases=('Education.person',),
        ),
    ]

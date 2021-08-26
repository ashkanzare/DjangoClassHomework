# Generated by Django 3.2.6 on 2021-08-24 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('unit', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='users_images')),
                ('entry_date', models.DateField()),
                ('study_field', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
            ],
            bases=('Education.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
                ('expertise', models.TextField(blank=True, null=True)),
                ('post', models.CharField(default=None, max_length=200, unique=True)),
            ],
            bases=('Education.person',),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('hours', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_stds', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('course_status', models.BooleanField(choices=[(True, 'Active'), (False, 'Ended')], default=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.college')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Education.lesson')),
                ('student', models.ManyToManyField(to='Education.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Education.teacher')),
            ],
        ),
    ]

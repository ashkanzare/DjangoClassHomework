# Generated by Django 3.2.6 on 2021-09-14 19:35

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
                ('first_name', models.CharField(max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('birthday', models.DateField(verbose_name='تاریخ تولد')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('personal_id', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='شماره شناسنامه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('entry_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ورود')),
                ('register_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ ثبت نام')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
                ('expertise', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, default=None, max_length=200, null=True, unique=True)),
            ],
            bases=('Education.person',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
                ('registration_confirmation', models.BooleanField(default=False, verbose_name='تایید ثبت نام')),
                ('max_units', models.PositiveIntegerField(default=24, verbose_name='حداکثر تعداد واحد')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Education.college')),
            ],
            options={
                'permissions': [('can_write_blog', 'Can Write Blog')],
            },
            bases=('Education.person',),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Education.person')),
                ('expertise', models.CharField(blank=True, max_length=200, null=True)),
                ('post', models.CharField(blank=True, default=None, max_length=200, null=True, unique=True)),
            ],
            bases=('Education.person',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='شماره تماس باید با فرمت ۹۱۲۷۸۹۳۴۵۶ وارد شود', regex='^9\\d{9}$')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image')),
                ('user_type', models.CharField(choices=[('boss', 'رییس'), ('staff', 'کارمند'), ('teacher', 'استاد'), ('student', 'دانشجو')], default=None, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='رشته تحصیلی')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='study_fields', to='Education.college')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_stds', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('course_status', models.BooleanField(choices=[(True, 'Active'), (False, 'Ended')], default=True)),
                ('session_1', models.CharField(blank=True, choices=[('شنبه', 'saturday'), ('یک شنبه', 'sunday'), ('دو شنبه', 'monday'), ('سه شنبه', 'thursday'), ('چهارشنبه', 'wednesday'), ('پنج شنبه', 'tuesday')], max_length=100, null=True)),
                ('session_2', models.CharField(blank=True, choices=[('شنبه', 'saturday'), ('یک شنبه', 'sunday'), ('دو شنبه', 'monday'), ('سه شنبه', 'thursday'), ('چهارشنبه', 'wednesday'), ('پنج شنبه', 'tuesday')], max_length=100, null=True)),
                ('session_start_time', models.TimeField(default=django.utils.timezone.now)),
                ('session_end_time', models.TimeField(default=django.utils.timezone.now)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.college')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Education.lesson')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Education.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='AllowedField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.course')),
                ('study_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Education.studyfield')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='Education.course')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.RESTRICT, to='Education.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='study_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='Education.studyfield', verbose_name='رشته تحصیلی'),
        ),
    ]

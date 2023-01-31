# Generated by Django 4.1.1 on 2022-11-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('phone_number', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Details_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('allergies', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_name', models.CharField(max_length=100)),
                ('ser_description', models.TextField()),
                ('ser_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Time_slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200)),
                ('doc_spec', models.CharField(max_length=200)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('ser_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.services')),
            ],
        ),
        migrations.CreateModel(
            name='Details_Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('year_of_experience', models.CharField(blank=True, max_length=200, null=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, max_length=200, null=True)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('description', models.TextField(blank=True)),
                ('doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.doctors')),
                ('time_slot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home_app.time_slot')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.patient')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.time_slot')),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-14 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career_Profile',
            fields=[
                ('career_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('contraction', models.CharField(max_length=7)),
                ('without_pressure', models.BooleanField(default=True)),
                ('lenght_in_months', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Personal_Data',
            fields=[
                ('curp', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('father_lastname', models.CharField(max_length=20)),
                ('mother_lastname', models.CharField(max_length=20)),
                ('names', models.CharField(max_length=40)),
                ('sex', models.CharField(choices=[('F', 'f'), ('M', 'f')], max_length=1)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Academic_Profile',
            fields=[
                ('register_number', models.AutoField(primary_key=True, serialize=False)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.career_profile')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.student_personal_data')),
            ],
        ),
    ]
# Generated by Django 3.2.12 on 2024-02-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('age', models.ImageField(upload_to='')),
                ('contact', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]

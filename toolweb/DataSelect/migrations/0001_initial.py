# Generated by Django 2.0.5 on 2018-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=50, verbose_name='filename')),
                ('colname', models.CharField(max_length=50, verbose_name='colname')),
                ('check_status', models.CharField(choices=[('C', 'Checked'), ('U', 'Unchecked')], max_length=4, verbose_name='col_status')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
            ],
            options={
                'verbose_name': 'DataSelect',
                'verbose_name_plural': 'DataSelect',
            },
        ),
    ]
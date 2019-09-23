# Generated by Django 2.0.5 on 2019-02-05 11:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crn_comm_date', models.DateField()),
                ('crn_clos_date', models.DateField()),
                ('cr_note', models.CharField(max_length=250)),
                ('cr_cash', models.IntegerField()),
                ('cr_status', models.CharField(default='Delivered', max_length=250)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('cr_station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='station.Station')),
            ],
        ),
    ]

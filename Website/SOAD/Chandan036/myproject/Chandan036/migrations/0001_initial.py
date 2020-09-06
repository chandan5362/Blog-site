# Generated by Django 3.1 on 2020-08-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abhisarga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=25, verbose_name='Name')),
                ('eventdate', models.DateTimeField(verbose_name='EventDate')),
                ('cordinator', models.CharField(max_length=25)),
                ('venue', models.CharField(max_length=25)),
                ('eventtype', models.CharField(max_length=55)),
                ('max_num_participants', models.IntegerField()),
                ('event_rule', models.TextField(blank=True)),
                ('event_prize', models.TextField(blank=True)),
            ],
        ),
    ]
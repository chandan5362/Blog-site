# Generated by Django 3.1 on 2020-08-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20200827_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('Home', 'Home'), ('Data Science', 'Datascience'), ('Machine Learning', 'Machinelearning'), ('Statistics', 'Statistics'), ('Project', 'Projects')], default='Home', max_length=50),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_student_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.IntegerField(choices=[(2020, '2020'), (2019, '2019'), (2018, '2018'), (2017, '2017'), (2016, '2016')], default=2020),
        ),
    ]

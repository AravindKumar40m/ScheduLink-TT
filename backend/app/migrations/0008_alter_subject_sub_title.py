# Generated by Django 4.2.6 on 2023-11-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_subject_reg_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_title',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-02 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('santech', '0006_rename_work_title_ourworks_works_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourworks',
            options={'verbose_name': 'Наши работы', 'verbose_name_plural': 'Наши работы'},
        ),
    ]

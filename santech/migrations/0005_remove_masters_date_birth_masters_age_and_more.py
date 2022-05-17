# Generated by Django 4.0.4 on 2022-04-28 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santech', '0004_alter_applicationstypes_applications_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masters',
            name='date_birth',
        ),
        migrations.AddField(
            model_name='masters',
            name='age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='filesforworks',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files_works/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='masters',
            name='work_experience',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.CreateModel(
            name='ImageForMasters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_masters/%Y/%m/%d')),
                ('for_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='santech.masters')),
            ],
            options={
                'db_table': 'Фото мастеров',
            },
        ),
    ]

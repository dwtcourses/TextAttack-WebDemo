# Generated by Django 3.1.3 on 2020-11-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdemo', '0006_auto_20201103_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackresult',
            name='input_label',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attackresult',
            name='output_label',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]

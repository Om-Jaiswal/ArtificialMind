# Generated by Django 4.0.6 on 2022-08-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagetranslate', '0002_multipleimage_lang'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multipleimage',
            old_name='lang',
            new_name='ilang',
        ),
        migrations.AddField(
            model_name='multipleimage',
            name='tlang',
            field=models.CharField(default='English', max_length=1000000),
        ),
    ]

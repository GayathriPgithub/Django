# Generated by Django 4.1.3 on 2023-01-28 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0006_rename_device_productinstance_medicalequipment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalequipment',
            options={'ordering': ['name', 'brand']},
        ),
    ]

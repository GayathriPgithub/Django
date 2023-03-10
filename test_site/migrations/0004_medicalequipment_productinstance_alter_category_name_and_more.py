# Generated by Django 4.1.3 on 2023-01-17 17:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0003_medical_device_delete_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1500)),
                ('price', models.IntegerField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_site.brand')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular Device', primary_key=True, serialize=False)),
                ('date_of_upload', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('i', 'In stock'), ('o', 'Out of stock')], help_text='Device availability', max_length=1)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='test_site.medicalequipment')),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Device Category (e.g. Radiology)', max_length=200),
        ),
        migrations.DeleteModel(
            name='Medical_Device',
        ),
        migrations.AddField(
            model_name='medicalequipment',
            name='category',
            field=models.ManyToManyField(help_text='Select category for this device', to='test_site.category'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-08 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locn_id', models.CharField(max_length=10, unique=True)),
                ('dsp_locn', models.CharField(max_length=10, unique=True)),
                ('locn_brcd', models.CharField(max_length=10, unique=True)),
                ('create_date_time', models.DateTimeField(auto_now_add=True)),
                ('mod_date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
                'db_table': 'location',
                'ordering': ['locn_brcd'],
            },
        ),
        migrations.CreateModel(
            name='PalletJackMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallet_jack_id', models.CharField(max_length=20, unique=True)),
                ('create_date_time', models.DateTimeField(auto_now_add=True)),
                ('mod_date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Traspaletas',
                'db_table': 'pallet_jack_master',
                'ordering': ['pallet_jack_id'],
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_nbr', models.CharField(max_length=30, unique=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('received_at', models.DateTimeField(null=True)),
                ('palletized_at', models.DateTimeField(null=True)),
                ('located_at', models.DateTimeField(null=True)),
                ('despatched_at', models.DateTimeField(null=True)),
                ('received', models.BooleanField(default=False)),
                ('palletized', models.BooleanField(default=False)),
                ('located', models.BooleanField(default=False)),
                ('despatched', models.BooleanField(default=False)),
                ('create_date_time', models.DateTimeField(auto_now_add=True)),
                ('mod_date_time', models.DateTimeField(auto_now=True)),
                ('pallet_jack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_shipments_pallet_jack', to='base.palletjackmaster')),
                ('putaway_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_shipments_current_location', to='base.location')),
            ],
            options={
                'verbose_name_plural': 'Encargos',
                'db_table': 'shipment',
                'ordering': ['shipment_nbr'],
            },
        ),
        migrations.AddIndex(
            model_name='location',
            index=models.Index(fields=['locn_brcd', 'locn_id'], name='location_locn_br_a81e8d_idx'),
        ),
    ]

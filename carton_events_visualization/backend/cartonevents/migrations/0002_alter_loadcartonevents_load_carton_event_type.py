# Generated by Django 4.2 on 2023-04-28 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartonevents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadcartonevents',
            name='load_carton_event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='eventtypes', to='cartonevents.loadcartoneventtype'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-03 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id_rent', models.AutoField(primary_key=True, serialize=False)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('id_car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.cars')),
                ('id_cos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.customer')),
            ],
        ),
    ]

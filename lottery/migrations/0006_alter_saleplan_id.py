# Generated by Django 4.1.5 on 2023-01-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0005_alter_saleplan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleplan',
            name='Id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_alter_saleplan_lotterydate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saleplan',
            name='RegisterStartDate',
            field=models.DateTimeField(),
        ),
    ]
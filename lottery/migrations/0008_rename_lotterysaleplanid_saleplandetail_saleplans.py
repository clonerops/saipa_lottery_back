# Generated by Django 4.1.5 on 2023-01-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0007_saleplandetail_delete_lottery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saleplandetail',
            old_name='LotterySalePlanId',
            new_name='SalePlans',
        ),
    ]
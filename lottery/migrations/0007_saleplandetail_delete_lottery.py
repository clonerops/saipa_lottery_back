# Generated by Django 4.1.5 on 2023-01-16 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lottery', '0006_alter_saleplan_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalePlanDetail',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('AnnounceNo', models.IntegerField()),
                ('AnnounceRowNo', models.IntegerField()),
                ('CirculationNo', models.IntegerField()),
                ('CarRow', models.IntegerField()),
                ('MainCapacity', models.IntegerField()),
                ('ReserveCapacity', models.IntegerField()),
                ('WindDistance', models.IntegerField()),
                ('LotteryBaseNo', models.IntegerField()),
                ('Description', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('LastModified', models.DateTimeField(auto_now=True)),
                ('CreatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('LotterySalePlanId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salePlansDetails', to='lottery.saleplan')),
            ],
        ),
        migrations.DeleteModel(
            name='Lottery',
        ),
    ]

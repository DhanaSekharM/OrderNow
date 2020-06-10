# Generated by Django 2.1.7 on 2019-04-06 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190405_1729'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ad',
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_id',
            field=models.IntegerField(default=123, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
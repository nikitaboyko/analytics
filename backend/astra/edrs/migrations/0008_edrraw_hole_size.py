# Generated by Django 2.2.1 on 2019-07-23 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edrs', '0007_auto_20190630_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='edrraw',
            name='hole_size',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=15, null=True),
        ),
    ]

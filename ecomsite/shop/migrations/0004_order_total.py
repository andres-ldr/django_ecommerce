# Generated by Django 5.0.2 on 2024-02-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]

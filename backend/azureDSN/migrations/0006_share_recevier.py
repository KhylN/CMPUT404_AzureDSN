# Generated by Django 5.1.1 on 2024-11-02 21:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azureDSN', '0005_share'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='recevier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

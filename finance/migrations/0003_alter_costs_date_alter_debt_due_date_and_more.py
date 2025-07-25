# Generated by Django 5.1.3 on 2025-07-25 06:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0002_alter_debt_amount_alter_payment_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="costs",
            name="date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Sana"
            ),
        ),
        migrations.AlterField(
            model_name="debt",
            name="due_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="To'lov sanasi"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="To'lov sanasi"
            ),
        ),
    ]

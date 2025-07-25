# Generated by Django 5.2.1 on 2025-06-04 06:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("attendance", "0001_initial"),
        ("members", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="attendance",
            options={"ordering": ["-attended_at"]},
        ),
        migrations.AddConstraint(
            model_name="attendance",
            constraint=models.UniqueConstraint(
                condition=models.Q(("state", True)),
                fields=("member", "attended_at"),
                name="unique_attendance_member_per_day",
            ),
        ),
    ]

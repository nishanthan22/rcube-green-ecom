# Generated by Django 5.0.7 on 2024-07-14 23:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rcubeApp", "0004_alter_paymentmethod_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentmethod",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="method",
            field=models.CharField(default="Unknown", max_length=50),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="address",
            field=models.CharField(default="123 Default St", max_length=255),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="card_number",
            field=models.CharField(default="0000000000000000", max_length=20),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="city",
            field=models.CharField(default="Default City", max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="cvv",
            field=models.CharField(default="000", max_length=4),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="exp_month",
            field=models.CharField(default="01", max_length=2),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="exp_year",
            field=models.CharField(default="2025", max_length=4),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="full_name",
            field=models.CharField(default="John Doe", max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="name_on_card",
            field=models.CharField(default="John Doe", max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="state",
            field=models.CharField(default="Default State", max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="zip_code",
            field=models.CharField(default="00000", max_length=20),
        ),
        migrations.DeleteModel(
            name="Payment",
        ),
    ]

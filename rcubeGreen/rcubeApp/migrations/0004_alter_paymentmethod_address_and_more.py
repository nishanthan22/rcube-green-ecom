# Generated by Django 5.0.6 on 2024-07-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rcubeApp", "0003_paymentmethod_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethod",
            name="address",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="card_number",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="city",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="cvv",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="email",
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="exp_month",
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="exp_year",
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="full_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="method",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="name_on_card",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="state",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="zip_code",
            field=models.CharField(max_length=20),
        ),
    ]

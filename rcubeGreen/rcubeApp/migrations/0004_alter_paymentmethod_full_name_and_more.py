# Generated by Django 5.0.7 on 2024-07-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rcubeApp", "0003_remove_paymentmethod_details_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paymentmethod",
            name="full_name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="name_on_card",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="paymentmethod",
            name="zip_code",
            field=models.CharField(max_length=10),
        ),
    ]
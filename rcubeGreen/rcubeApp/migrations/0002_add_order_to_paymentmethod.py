from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('rcubeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='order',
            field=models.ForeignKey(null=True, on_delete=models.CASCADE, to='rcubeApp.Order'),
        ),
    ]

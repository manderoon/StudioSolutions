# Generated by Django 3.2.18 on 2023-04-16 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_id_number'),
        ('preferences', '0002_auto_20230416_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferences',
            name='p1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preferences_p1', to='products.product'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='p2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preferences_p2', to='products.product'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='p3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preferences_p3', to='products.product'),
        ),
    ]

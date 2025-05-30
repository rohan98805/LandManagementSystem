# Generated by Django 5.1.4 on 2025-05-15 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='land_images/')),
                ('land_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accounts.landrecord')),
            ],
        ),
    ]

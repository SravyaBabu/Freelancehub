# Generated by Django 5.1.6 on 2025-03-07 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_coderreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('time', models.CharField(max_length=100)),
                ('utype', models.CharField(max_length=100)),
                ('buyerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.buyer')),
                ('coderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.coder')),
            ],
        ),
    ]

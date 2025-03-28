# Generated by Django 5.1.6 on 2025-03-04 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_projects_assignstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoderReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.IntegerField()),
                ('feedback', models.CharField(max_length=400, null=True)),
                ('buyerid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.buyer')),
                ('coderid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.coder')),
            ],
        ),
    ]

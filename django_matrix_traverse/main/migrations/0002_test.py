# Generated by Django 5.0.2 on 2024-03-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_matrix', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'matrices',
            },
        ),
    ]
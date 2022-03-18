# Generated by Django 4.0.3 on 2022-03-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.TextField(verbose_name='Производитель')),
                ('model', models.TextField(verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Доступное оборудование',
                'verbose_name_plural': 'Доступное оборудование',
                'db_table': 'devices',
            },
        ),
    ]

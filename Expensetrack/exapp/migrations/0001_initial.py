# Generated by Django 3.2.6 on 2021-10-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
            ],
            options={
                'db_table': 'balance',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expensename', models.CharField(max_length=500)),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'expense',
            },
        ),
    ]

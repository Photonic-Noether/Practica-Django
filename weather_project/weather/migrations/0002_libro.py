# Generated by Django 5.0.7 on 2024-07-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=400)),
                ('paginas', models.IntegerField()),
            ],
        ),
    ]

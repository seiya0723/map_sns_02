# Generated by Django 3.2.10 on 2022-06-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='名前')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='緯度')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='経度')),
            ],
        ),
    ]

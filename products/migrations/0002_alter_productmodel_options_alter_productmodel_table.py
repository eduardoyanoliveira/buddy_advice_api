# Generated by Django 4.1.1 on 2022-09-30 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelTable(
            name='productmodel',
            table='tbl_products',
        ),
    ]
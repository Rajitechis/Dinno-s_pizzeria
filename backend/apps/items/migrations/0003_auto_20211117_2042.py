# Generated by Django 3.2.4 on 2021-11-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='message',
            field=models.CharField(db_index=True, default='Anonymous', max_length=200, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(db_index=True, default='Anonymous', max_length=30, verbose_name='Name'),
        ),
    ]
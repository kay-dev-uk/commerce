# Generated by Django 4.1 on 2022-10-07 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_alter_comment_date_alter_listing_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 7, 13, 49, 4, 239145)),
        ),
    ]

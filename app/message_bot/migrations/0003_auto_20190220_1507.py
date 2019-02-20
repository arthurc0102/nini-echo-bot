# Generated by Django 2.1.7 on 2019-02-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_bot', '0002_auto_20190220_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('AD', 'Add'), ('ED', 'Edit'), ('DE', 'Delete')], max_length=2),
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together={('user_id', 'chat_id')},
        ),
    ]

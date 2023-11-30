# Generated by Django 4.2.7 on 2023-11-30 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_user_address_user_address_and_more'),
        ('accounts', '0003_rename_account_amount_account_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
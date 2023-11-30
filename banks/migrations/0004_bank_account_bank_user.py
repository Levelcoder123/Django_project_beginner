# Generated by Django 4.2.7 on 2023-11-30 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_user'),
        ('users', '0003_rename_user_address_user_address_and_more'),
        ('banks', '0003_rename_bank_branch_bank_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='account',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AddField(
            model_name='bank',
            name='user',
            field=models.ManyToManyField(to='users.user'),
        ),
    ]

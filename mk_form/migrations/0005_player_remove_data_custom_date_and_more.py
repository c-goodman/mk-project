# Generated by Django 5.1.1 on 2024-09-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mk_form", "0004_data_custom_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(default="Cooper", max_length=20, unique=True),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="data",
            name="custom_date",
        ),
        migrations.AlterField(
            model_name="data",
            name="player_first",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Player (1st)"
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="player_fourth",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Player (4th)"
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="player_second",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Player (2nd)"
            ),
        ),
        migrations.AlterField(
            model_name="data",
            name="player_third",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Player (3rd)"
            ),
        ),
    ]

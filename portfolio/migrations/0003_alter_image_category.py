# Generated by Django 4.0.1 on 2022-03-28 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default='category', on_delete=django.db.models.deletion.CASCADE, to='portfolio.category'),
        ),
    ]

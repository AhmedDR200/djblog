# Generated by Django 4.2.3 on 2023-07-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_category_alter_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WB', 'web development'), ('DB', 'desktop development')], max_length=20),
        ),
    ]
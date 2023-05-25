# Generated by Django 4.2 on 2023-05-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auction_topic',
            fields=[
                ('auction_topic_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('title_auction_topic', models.CharField(max_length=100)),
                ('create_date_auction_topic', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=False)),
                ('is_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
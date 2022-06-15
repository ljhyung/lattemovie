# Generated by Django 3.2.12 on 2022-05-19 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.BooleanField()),
                ('backdrop_path', models.CharField(max_length=150)),
                ('genres', models.CharField(max_length=150)),
                ('original_language', models.CharField(max_length=150)),
                ('original_title', models.CharField(max_length=150)),
                ('overview', models.CharField(max_length=1000)),
                ('popularity', models.IntegerField()),
                ('poster_path', models.CharField(max_length=150)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('tagline', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
            ],
        ),
    ]
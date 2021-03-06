# Generated by Django 2.2.4 on 2020-02-01 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uscf_id', models.IntegerField(blank=True, null=True)),
                ('chesscom_id', models.CharField(blank=True, max_length=100, null=True)),
                ('lichess_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('min_rating', models.IntegerField(blank=True, null=True)),
                ('max_rating', models.IntegerField(blank=True, null=True)),
                ('hourly_rate_private', models.IntegerField(blank=True, null=True)),
                ('hourly_rate_group', models.IntegerField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ccc.Member')),
            ],
            options={
                'verbose_name_plural': 'coaches',
            },
        ),
    ]

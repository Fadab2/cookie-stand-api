# Generated by Django 4.0.3 on 2022-03-26 23:38

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
            name='CookieStand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('hourly_sales', models.JSONField(blank=True, default=list)),
                ('minimum_customers_per_hour', models.IntegerField(default=0)),
                ('maximum_customers_per_hour', models.IntegerField(default=0)),
                ('average_cookies_per_sale', models.FloatField(default=0)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

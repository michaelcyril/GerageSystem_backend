# Generated by Django 3.2.16 on 2023-04-01 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_auto_20230331_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.TextField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('garage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.garage')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
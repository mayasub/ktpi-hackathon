# Generated by Django 3.1.3 on 2020-12-03 22:21

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
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(blank=True)),
                ('pledgeClass', models.TextField(choices=[('Eldon', 'Eldon'), ('Omicron', 'Omicron'), ('Pi', 'Pi'), ('Rho', 'Rho'), ('Sigma', 'Sigma')], default='Eldon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 2.1.7 on 2019-05-25 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surveyhome', '0002_auto_20190525_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveytitle',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

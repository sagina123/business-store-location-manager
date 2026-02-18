from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_store_latitude_store_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='floor',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

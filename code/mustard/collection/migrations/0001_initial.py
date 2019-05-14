# Generated by Django 2.2.1 on 2019-05-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specimen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('collection_id', models.CharField(blank=True, default=None, max_length=100)),
                ('origin_local', models.CharField(blank=True, default=None, max_length=100)),
                ('chemistry', models.CharField(blank=True, default=None, max_length=100)),
                ('provenance', models.CharField(blank=True, default=None, max_length=100)),
                ('dana_classification', models.CharField(blank=True, default=None, max_length=30)),
                ('external_link', models.CharField(blank=True, default=None, max_length=100)),
            ],
            options={
                'ordering': ['collection_id'],
            },
        ),
    ]
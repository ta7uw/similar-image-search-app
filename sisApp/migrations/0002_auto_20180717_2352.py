# Generated by Django 2.0.7 on 2018-07-17 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sisApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded', verbose_name='uploaded image')),
            ],
            options={
                'db_table': 'UploadedImage',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='origin', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterModelTable(
            name='item',
            table='Item',
        ),
    ]

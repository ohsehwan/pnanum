# Generated by Django 2.1.4 on 2019-01-18 01:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('html', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='사진')),
                ('file', models.FileField(blank=True, null=True, upload_to='files', verbose_name='파일')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
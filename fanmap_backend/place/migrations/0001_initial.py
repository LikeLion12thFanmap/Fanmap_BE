# Generated by Django 5.0.6 on 2024-06-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=128, verbose_name='위치')),
                ('pName', models.CharField(max_length=200, verbose_name='장소이름')),
                ('purpose', models.CharField(max_length=128, verbose_name='장소 목적')),
                ('sTime', models.DateField(verbose_name='활성화시작시간')),
                ('eTime', models.DateField(verbose_name='활성화종료시간')),
                ('basic_cate', models.CharField(max_length=200, verbose_name='기본카테고리')),
                ('detail_cate', models.CharField(max_length=200, verbose_name='세부카테고리')),
                ('require', models.CharField(blank=True, max_length=300, null=True, verbose_name='필요조건')),
                ('link', models.URLField(blank=True, null=True, verbose_name='링크')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='place_image', verbose_name='대표이미지')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='place_image', verbose_name='이미지1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='place_image', verbose_name='이미지2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='place_image', verbose_name='이미지3')),
            ],
        ),
    ]
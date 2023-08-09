# Generated by Django 4.2 on 2023-08-09 20:47

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NecessaryLink',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.URLField(verbose_name='Обязательная ссылка')),
                ('telegram_link_id', models.BigIntegerField(verbose_name='id КАНАЛА/ЧАТА - ОБЯЗАТЕЛЬНО')),
                ('title', models.CharField(max_length=50, verbose_name='Название кнопки - ОБЯЗАТЕЛЬНО. Можно смайлики')),
            ],
            options={
                'verbose_name': 'Необходимая ссылка',
                'verbose_name_plural': 'Необходимые ссылки',
            },
        ),
        migrations.CreateModel(
            name='SettingModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('telegram_id', models.PositiveBigIntegerField(default=1, unique=True, verbose_name='ID пользователя Телеграм')),
                ('technical_works', models.BooleanField(default=False, verbose_name='Технические работы')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telegram_id', models.PositiveBigIntegerField(default=1, unique=True, verbose_name='ID пользователя Телеграм')),
                ('name', models.CharField(max_length=255, verbose_name='Имя пользователя')),
                ('username', models.CharField(max_length=255, verbose_name='Username Telegram')),
                ('sex', models.CharField(blank=True, max_length=30, null=True, verbose_name='Пол искателя')),
                ('age', models.BigIntegerField(blank=True, null=True, verbose_name='Возраст искателя')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город искателя')),
                ('need_city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город партнера')),
                ('need_distance', models.PositiveIntegerField(blank=True, null=True, verbose_name='Расстояние между партнерами')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='координаты пользователя')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='координаты пользователя')),
                ('verification', models.BooleanField(default=False, verbose_name='Верификация')),
                ('language', models.CharField(blank=True, max_length=10, null=True, verbose_name='Язык пользователя')),
                ('varname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Публичное имя пользователя')),
                ('lifestyle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Стиль жизни пользователя')),
                ('is_banned', models.BooleanField(default=False, verbose_name='Забанен ли пользователь')),
                ('photo_id', models.CharField(max_length=400, null=True, verbose_name='Photo_ID')),
                ('commentary', models.CharField(blank=True, max_length=300, null=True, verbose_name='Комментарий пользователя')),
                ('need_partner_sex', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пол партнера')),
                ('need_partner_age_min', models.PositiveIntegerField(default=16, verbose_name='Минимальный возраст партнера')),
                ('need_partner_age_max', models.PositiveIntegerField(default=24, verbose_name='Максимальный возраст партнера')),
                ('referrer_id', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='реферал')),
                ('phone_number', models.BigIntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('status', models.BooleanField(default=False, verbose_name='Статус анкеты')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ник в инстаграме')),
                ('events', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), default=list, size=None)),
                ('id_of_events_seen', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=list, size=None)),
            ],
            options={
                'verbose_name': ('Пользователь Знакомств',),
                'verbose_name_plural': 'Пользователи Знакомств',
            },
        ),
        migrations.CreateModel(
            name='UserMeetings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('telegram_id', models.PositiveBigIntegerField(default=1, unique=True, verbose_name='ID пользователя Телеграм')),
                ('username', models.CharField(max_length=255, verbose_name='Username Telegram')),
                ('commentary', models.CharField(max_length=50, null=True, verbose_name='Комментарий')),
                ('time_event', models.CharField(max_length=10, null=True, verbose_name='Время проведения')),
                ('venue', models.CharField(max_length=50, null=True, verbose_name='Место проведения')),
                ('need_location', models.CharField(max_length=50, null=True)),
                ('event_name', models.CharField(max_length=50, null=True, verbose_name='Название мероприятия')),
                ('verification_status', models.BooleanField(default=False, verbose_name='Статус пользователя')),
                ('moderation_process', models.BooleanField(default=True, verbose_name='Процесс модерации')),
                ('is_premium', models.BooleanField(default=False, verbose_name='Премиум')),
                ('photo_id', models.CharField(max_length=400, null=True, verbose_name='Photo_ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': ('Пользователь Мероприятий',),
                'verbose_name_plural': 'Пользователи Мероприятий',
            },
        ),
        migrations.CreateModel(
            name='ViewedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='usersmanage.user')),
                ('viewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to='usersmanage.user')),
            ],
            options={
                'unique_together': {('viewer', 'profile')},
            },
        ),
        migrations.AddField(
            model_name='user',
            name='viewed_profiles',
            field=models.ManyToManyField(through='usersmanage.ViewedProfile', to='usersmanage.user'),
        ),
    ]

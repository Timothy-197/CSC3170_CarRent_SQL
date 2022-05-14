# Generated by Django 4.0.4 on 2022-05-09 01:05

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
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=8)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'owner',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userIcon_url', models.ImageField(default='UserIcon/default.png', upload_to='UserIcon/')),
                ('userIntro', models.CharField(default='He is BUSY in doing CSC4001 project! Nothing Left!', max_length=300)),
                ('userJob', models.CharField(default='Programming', max_length=30)),
                ('userHobby', models.CharField(default='Running', max_length=30)),
                ('userMobile', models.CharField(default='15857358070', max_length=15)),
                ('user_is_customer', models.IntegerField(default=1)),
                ('userLocation', models.CharField(default='The Chinise University of Hong Kong, Shenzhen', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfile',
                'verbose_name_plural': 'UserProfile Management',
            },
        ),
    ]

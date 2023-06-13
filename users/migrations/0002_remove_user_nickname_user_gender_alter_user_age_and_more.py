# Generated by Django 4.2.2 on 2023-06-12 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', '남자'), ('female', '여자')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='login_type',
            field=models.CharField(choices=[('normal', '일반'), ('kakao', '카카오'), ('google', '구글'), ('naver', '네이버')], default='normal', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fridges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
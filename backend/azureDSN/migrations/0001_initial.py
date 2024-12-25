# Generated by Django 5.1.1 on 2024-10-30 04:11

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('require_approval', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('type', models.TextField(default='author', editable=False)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.URLField(null=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('display_name', models.CharField(max_length=20)),
                ('github', models.URLField(null=True)),
                ('page', models.URLField(null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remote_follower', models.URLField(blank=True, null=True)),
                ('remote_followee', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='date followed')),
                ('local_followee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_followee', to=settings.AUTH_USER_MODEL)),
                ('local_follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='local_follower', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FollowRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(default='follow', editable=False)),
                ('actor', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InboxItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.UUIDField(blank=True, null=True)),
                ('remote_payload', models.JSONField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(to='azureDSN.inboxitem')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('type', models.TextField(default='post', editable=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('has_image', models.BooleanField(default=False)),
                ('content_type', models.CharField(choices=[('text/plain', 'UTF-8'), ('text/markdown', 'CommonMark'), ('image/png;base64', 'PNG Image (Base64)'), ('image/jpeg;base64', 'JPEG Image (Base64)'), ('application/base64', 'Other Base64 Data')], default='text/plain', max_length=20)),
                ('content', models.TextField(blank=True, null=True)),
                ('visibility', models.IntegerField(choices=[(1, 'PUBLIC'), (2, 'FRIENDS'), (3, 'UNLISTED'), (4, 'DELETED')], default=1)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='date posted')),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('type', models.TextField(default='like', editable=False)),
                ('user', models.JSONField(default=dict)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='date liked')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azureDSN.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('type', models.TextField(default='comment', editable=False)),
                ('user', models.JSONField(db_column='user', default=dict)),
                ('comment', models.CharField(max_length=500)),
                ('contentType', models.TextField(default='text/plain')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='date commented')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azureDSN.post')),
            ],
        ),
    ]

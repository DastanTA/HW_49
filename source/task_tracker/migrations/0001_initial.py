# Generated by Django 4.1.3 on 2022-11-18 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(choices=[('new', 'новый'), ('in progress', 'в процессе'), ('done', 'выполнено')], default='new', max_length=40, verbose_name='название статуса')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('task', 'задача'), ('bug', 'ошибка'), ('enhancement', 'улучшение')], default='task', max_length=40, verbose_name='название типа')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=40, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='время изменения')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='statuses', to='task_tracker.status', verbose_name='статус')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='типы', to='task_tracker.type', verbose_name='тип')),
            ],
        ),
    ]
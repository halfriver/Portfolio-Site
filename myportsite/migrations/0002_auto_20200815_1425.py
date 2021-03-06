# Generated by Django 3.0.5 on 2020-08-15 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myportsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='date_due',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='recur_interval',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TodoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='New To-Do', max_length=30)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myportsite.Board')),
            ],
        ),
        migrations.AddField(
            model_name='todolist',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myportsite.TodoGroup'),
        ),
    ]

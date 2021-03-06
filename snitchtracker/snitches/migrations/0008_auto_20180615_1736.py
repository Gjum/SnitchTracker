# Generated by Django 2.0.6 on 2018-06-15 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snitches', '0007_auto_20180613_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('x_pos', models.IntegerField(default=0)),
                ('y_pos', models.IntegerField(default=0)),
                ('z_pos', models.IntegerField(default=0)),
                ('world', models.CharField(max_length=100)),
                ('server', models.CharField(max_length=100)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snitches.Token')),
            ],
        ),
        migrations.CreateModel(
            name='Snitch_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(default=None, verbose_name='date published')),
                ('snitch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snitches.Snitch')),
            ],
        ),
        migrations.RemoveField(
            model_name='webhooktransaction',
            name='group',
        ),
        migrations.AddField(
            model_name='webhooktransaction',
            name='token',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='snitches.Token'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group_member',
            name='permission',
            field=models.CharField(choices=[(0, 'Admin'), (1, 'Member')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='snitch_group',
            name='snitch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snitches.Snitch'),
        ),
        migrations.DeleteModel(
            name='Snitch_Details',
        ),
    ]

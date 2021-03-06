# Generated by Django 3.2.4 on 2021-06-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=100)),
                ('book_press', models.CharField(max_length=100)),
                ('book_category', models.CharField(choices=[('1', '法律'), ('2', '人文'), ('3', '综合'), ('4', '理工'), ('5', '机械'), ('6', '财经'), ('7', '经济'), ('8', '政治'), ('9', '生物'), ('10', '商业'), ('11', '科学')], max_length=4)),
                ('book_year', models.CharField(max_length=10)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('book_stock_nums', models.IntegerField(max_length=3)),
                ('book_borrow_nums', models.IntegerField(max_length=3)),
                ('book_create_data', models.DateTimeField(verbose_name='create_date')),
            ],
        ),
        migrations.CreateModel(
            name='BookUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=11)),
                ('book_id', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100, unique=True)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_phone', models.CharField(max_length=11)),
                ('user_number', models.CharField(max_length=20, unique=True)),
                ('user_class', models.CharField(max_length=20)),
                ('user_major', models.CharField(max_length=20)),
                ('user_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('user_password', models.CharField(max_length=20)),
            ],
        ),
    ]

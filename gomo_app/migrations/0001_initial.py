# Generated by Django 3.2.8 on 2021-10-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=26)),
                ('account', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
                ('available_payment_method_details', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DashBoardBillList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=16)),
                ('bill_name', models.CharField(max_length=25)),
                ('bill_icon_image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentConfirmationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=17)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=13)),
                ('last_name', models.CharField(max_length=13)),
                ('phone_number', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=25)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UploadBillPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
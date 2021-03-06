# Generated by Django 3.0.1 on 2020-01-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191228_1233'),
        ('product', '0007_products_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='question',
            field=models.ManyToManyField(related_name='product_questions_set', through='product.ProductQuestions', to='user.Users'),
        ),
        migrations.AddField(
            model_name='products',
            name='user_like',
            field=models.ManyToManyField(related_name='user_like_products_set', through='product.UserLikeProducts', to='user.Users'),
        ),
    ]

# Generated by Django 4.2.2 on 2024-08-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'permissions': [('can_unpublish_product', 'Можно отменить публикацию продукта'), ('can_edit_product_description', 'Можно менять описание любого продукта'), ('can_change_product_category', 'Можно изменить категорию продукта')], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]

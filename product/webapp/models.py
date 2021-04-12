from django.db import models

category_choices=(
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('stationary', 'Концелярие'),
    ('cosmetics', 'Косметика'),
    ('other', 'Разное')
)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=2000, null=True, blank=True)
    category = models.CharField(max_length=300, default="other", choices=category_choices, blank=True, null=True)
    remainder = models.PositiveSmallIntegerField(null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.description, self.category)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = "продукты"


class Basket(models.Model):
    product = models.ForeignKey(Product,related_name='baskets',on_delete=models.DO_NOTHING)
    amount = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = "Товары в корзине"


class Order(models.Model):
    goods = models.ManyToManyField(Product,related_name='orders')
    username = models.CharField(max_length=200, blank=False,null=False)
    telephone = models.CharField(max_length=200, blank=False,null=False)
    adress = models.CharField(max_length=200, blank=False,null=False)
    datetimes = models.DateTimeField('date',auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"

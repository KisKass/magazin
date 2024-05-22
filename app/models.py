from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name="Название")
    class Meta:

        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name} '


class Item(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Категория")
    name = models.CharField(max_length=150,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(decimal_places=2, max_digits=6,verbose_name="Цена")
    image = models.ImageField(upload_to="items",verbose_name="Изображение")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.name} '


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE,verbose_name="Корзина")
    item = models.ForeignKey(Item, related_name='cart_item', on_delete=models.CASCADE,verbose_name="Товар")
    quantity = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.cart_id} {self.item.name} '


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,verbose_name="Пользователь")
    items = models.ManyToManyField(Item, through=CartItem,verbose_name="Товары")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f'ID:{self.id} | {self.user} '


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    email = models.EmailField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Пользователь")
    phone_number = models.CharField(max_length=150,verbose_name="Номер телефона")
    name = models.CharField(max_length=150,verbose_name="Имя")
    address = models.CharField(max_length=150,verbose_name="Адрес")
    email = models.EmailField(verbose_name="Адрес электронной почты")
    extra_info = models.EmailField(verbose_name="Дополнительная информация")
    date = models.DateField(verbose_name="Дата заказа")
    status = models.CharField(max_length=100,verbose_name="Статус")
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, verbose_name="Корзина")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'ID:{self.user} | {self.date} | Статус - {self.status}'
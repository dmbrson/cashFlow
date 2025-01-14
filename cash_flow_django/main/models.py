from django.db import models

class Status(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="categories", verbose_name="Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class SubCategory(models.Model):
    name = models.CharField('Название', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories", verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class CashFlowRecord(models.Model):
    created_at = models.DateField('Создано')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Статус")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Тип")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=0)
    comment = models.TextField('Комментарий', blank=True, null=True)

    def __str__(self):
        return f"{self.created_at}, {self.category.name}, {self.subcategory.name}, {self.type.name} {self.amount}р"

    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'
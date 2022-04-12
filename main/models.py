from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy
from .validators import validate_file_extensions


class Collection(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images", null=True, blank=True)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.title


class Product(models.Model):
    collection = models.ForeignKey(Collection, verbose_name="Коллекция",
                                   on_delete=models.SET_NULL, null=True, related_name="products")
    title = models.CharField(max_length=255)
    articul = models.CharField(max_length=255, unique=True)
    colors = models.ManyToManyField(Color)
    price = models.IntegerField()
    old_price = models.IntegerField(null=True)
    description = models.TextField()
    size = models.TextField()
    material_composition = models.TextField()
    quantity_in_one_line = models.IntegerField()
    fabric = models.CharField(max_length=255)
    is_hit_of_sales = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name="Изображения", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/", null=True)


class News(models.Model):
    image = models.ImageField(upload_to="news_images/", blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Новости"
        ordering = ("id", )


class Help(models.Model):
    question = models.CharField("Вопрос", max_length=255)
    answer = models.CharField(max_length=255)
    image = models.ImageField(upload_to="help_images/", blank=True, null=True)

    def __str__(self):
        return f"Вопрос №{self.pk}"

    class Meta:
        verbose_name = "Помощь"
        verbose_name_plural = "Помощь"


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class AboutUsImage(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name="images")


class PublicOffer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публичная оферта"
        verbose_name_plural = "Публичная оферта"


class OurContacts(models.Model):
    whatsapp = models.CharField(max_length=255)
    telegram = models.CharField("Номер в телеграм", max_length=255)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.whatsapp = "https://whatsapp/" + slugify(self.whatsapp)
        self.telegram = "https://telegram/" + slugify(self.telegram)
        return super(OurContacts, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Наши контакты"
        verbose_name_plural = "Наши контакты"


class CallbackRequest(models.Model):
    class DidCallback(models.TextChoices):
        # yes = "Y", gettext_lazy("Yes")
        # no = "N", gettext_lazy("No")
        yes = gettext_lazy("Yes")
        no = gettext_lazy("No")

    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    type_of_appeal = models.CharField(max_length=255, default="Обратный звонок")
    did_callback = models.CharField(max_length=255, choices=DidCallback.choices, default=DidCallback.no)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Обратный звонок"
        verbose_name_plural = "Обратные звонки"


class Slider(models.Model):
    image = models.ImageField(upload_to="slider_image/")

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class OurAdvantages(models.Model):
    icon = models.ImageField('Image', upload_to="our_advantages/", validators=[validate_file_extensions])
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Наши преимущества"
        verbose_name_plural = "Наши преимущества"


class Footer1th(models.Model):
    logo = models.ImageField(upload_to="logos/")
    text_field = models.TextField()

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футер"


class Footer2th(models.Model):
    pass

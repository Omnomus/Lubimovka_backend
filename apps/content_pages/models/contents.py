from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from apps.core.models import BaseModel


class AbstractContentPage(BaseModel):
    """Шаблон модели с конструктором.

    Для создания полноценной модели с конструктором создайте две новые модели
    унаследовав их от 'AbstractContentPage' и 'AbstractContent'.

    Модель обладает обычными полями (title, description). К ней подключается
    блок с конструктором.
    """

    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок страницы",
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание страницы",
    )

    class Meta:
        abstract = True
        verbose_name = "Шаблон объекта с сложной версткой"
        verbose_name_plural = "Шаблоны объектов с сложной версткой"
        ordering = ("-modified",)

    def __str__(self):
        return self.title


class AbstractContent(models.Model):
    """Шаблон базового блока конструктора.

    При наследовании укажите модель к которой будут подключаться блоки
    конструктора (реальную модель вместо 'AbstractContentPage' в поле
    'content_page').

    Для ограничения количества типов объектов в конструкторе задайте их список
    переопределив поле 'content' и атрибут 'limit_choices_to'.

    Описание полей:
        1. 'content_page' - foreign key для подключения к родительской
            'AbstractContentPage' модели
        2. 'item' - элемент 'контента'. Так как элементы контента могут быть
            разных типов реализуется с помощью ключа GenereForeginKey и двух
            дополнительных полей.
                - content_type = указывает на модель с типом контента
                - object_id = указывает на id объекта типа 'content_type'
            Т.е. 3 поля в сумме дают GenereForeginKey.
            Если остаются вопросы по реализации пожалуйста смотрите
            документацию django.
        3. 'order' — поле для упорядочивания блоков конструктора относительно
            родительского 'AbstractContentPage' объекта.
    """

    content_page = models.ForeignKey(
        AbstractContentPage,
        related_name="contents",
        on_delete=models.CASCADE,
        verbose_name="Страница с конструктором",
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"app_label": "content_pages"},
        verbose_name="Тип объекта",
    )
    object_id = models.PositiveIntegerField(
        verbose_name="ID объекта",
    )
    item = GenericForeignKey()
    order = models.PositiveSmallIntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок",
    )

    class Meta:
        abstract = True
        ordering = ("order",)
        verbose_name = "Блок/элемент конструктора"
        verbose_name_plural = "Блоки/элементы конструктора"

    def __str__(self):
        return f"Блок/элемент — {self.item}"

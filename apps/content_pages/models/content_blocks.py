from django.db import models

from apps.content_pages.models import AbstractItemWithTitle, Image, Video
from apps.core.models import BaseModel
from apps.library.models import Performance, Person, Play


class AbstractOrderedItemBase(BaseModel):
    """Abstract 'through' model for 'contet' blocks with ordered items.

    It's required that inherited models have to have 'item' and 'base' fields.
    It's good idea to check it during class initialization but haven't
    find how to do it for now.
    """

    order = models.PositiveIntegerField(
        default=0, blank=False, null=False, verbose_name="Порядок в блоке"
    )

    class Meta:
        verbose_name = "Содержимое блока"
        verbose_name_plural = "Содержимое блоков"
        abstract = True
        ordering = ("order",)

    def __str__(self):
        return f"{self.order} — {self.item}"


class OrderedImage(AbstractOrderedItemBase):
    item = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="ordered_images",
        verbose_name="Изображение",
    )
    block = models.ForeignKey(
        "ImagesBlock",
        on_delete=models.CASCADE,
        related_name="ordered_images",
    )


class OrderedPerformance(AbstractOrderedItemBase):
    item = models.ForeignKey(
        Performance,
        on_delete=models.CASCADE,
        related_name="ordered_performances",
        verbose_name="Спектакль",
    )
    block = models.ForeignKey(
        "PerformancesBlock",
        on_delete=models.CASCADE,
        related_name="ordered_performances",
    )


class OrderedPerson(AbstractOrderedItemBase):
    item = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="ordered_persons",
        verbose_name="Персона/человек",
    )
    block = models.ForeignKey(
        "PersonsBlock",
        on_delete=models.CASCADE,
        related_name="ordered_persons",
    )


class OrderedPlay(AbstractOrderedItemBase):
    item = models.ForeignKey(
        Play,
        on_delete=models.CASCADE,
        related_name="ordered_plays",
        verbose_name="Пьеса",
    )
    block = models.ForeignKey(
        "PlaysBlock",
        on_delete=models.CASCADE,
        related_name="ordered_plays",
    )


class OrderedVideo(AbstractOrderedItemBase):
    item = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,
        related_name="ordered_videos",
        verbose_name="Видео",
    )
    block = models.ForeignKey(
        "VideosBlock",
        on_delete=models.CASCADE,
        related_name="ordered_videos",
    )


class ImagesBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Image,
        through=OrderedImage,
        related_name="image_blocks",
    )

    class Meta:
        verbose_name = "Блок изображения"
        verbose_name_plural = "Блоки изображений"


class PerformancesBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Performance,
        through=OrderedPerformance,
        related_name="performance_blocks",
    )

    class Meta:
        verbose_name = "Блок спектаклей"
        verbose_name_plural = "Блоки спектаклей"


class PersonsBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Person,
        through=OrderedPerson,
        related_name="person_blocks",
    )

    class Meta:
        verbose_name = "Блок персон"
        verbose_name_plural = "Блоки персон"


class PlaysBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Play,
        through=OrderedPlay,
        related_name="play_blocks",
    )

    class Meta:
        verbose_name = "Блок пьес"
        verbose_name_plural = "Блоки пьес"


class VideosBlock(AbstractItemWithTitle):
    items = models.ManyToManyField(
        to=Video,
        through=OrderedVideo,
        related_name="video_blocks",
    )

    class Meta:
        verbose_name = "Блок видео"
        verbose_name_plural = "Блоки видео"

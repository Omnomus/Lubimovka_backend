# Generated by Django 3.2.8 on 2021-11-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaticPagesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(
                        max_length=30,
                        unique=True,
                        verbose_name="Название страницы",
                    ),
                ),
                (
                    "static_page_url",
                    models.SlugField(
                        max_length=30,
                        unique=True,
                        verbose_name="Путь к странице",
                    ),
                ),
                (
                    "data",
                    models.TextField(
                        help_text="\n            Для того, чтобы загрузить картинку, перетащите её в поле.\n            Как пользоваться разметкой Markdown, нажмите <a href='https://www.markdownguide.org/basic-syntax/'>СЮДА</a>.\n            ",
                        verbose_name="Данные, отображаемые на странице",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статическая страница",
                "verbose_name_plural": "Статические страницы",
            },
        ),
    ]

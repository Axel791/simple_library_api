from django.db import models


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name="Имя автора")
    last_name = models.CharField(max_length=50, null=False, verbose_name="Фамилия автора")
    date_of_birth = models.DateField(verbose_name="Дата рождения", null=True)
    date_of_death = models.DateField(verbose_name="Дата смерти", null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    class Meta:
        db_table = "author"

    def __str__(self):
        return self.first_name


class Book(models.Model):
    DRAFT = "DR"
    PUBLISHED = "PB"
    DELETED = "DL"

    BOOK_STATUS = [
        (DRAFT, "На модерации"),
        (PUBLISHED, "Опубликована"),
        (DELETED, "Удалена")
    ]

    name = models.CharField(max_length=30, null=False, verbose_name="Название книги")
    description = models.CharField(max_length=500, null=False, verbose_name="Описание")
    page_count = models.IntegerField(null=False, verbose_name="Кол-во страниц")
    created_at = models.DateTimeField(auto_now_add=True)
    book_status = models.CharField(
        max_length=2,
        choices=BOOK_STATUS,
        default=DRAFT,
        verbose_name="Статус публикации"
    )
    author = models.ForeignKey(
        BookAuthor,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        verbose_name="Имя автора"
    )

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

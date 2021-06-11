from django.db import models
import uuid
from apps.accounts.models import MyUser as User


class Company(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'О компании'

    def __str__(self):
        return self.title


class Contact(models.Model):
    phone_number = models.CharField(max_length=20,
                                    verbose_name='Номер телефона')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания',
                                related_name='contacts')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class SocialMedia(models.Model):
    media_name = models.CharField(max_length=150,
                                  verbose_name='Социальная сеть')
    url = models.URLField(verbose_name='Ссылка')
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                verbose_name='Компания',
                                related_name='medias')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.media_name


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=5, decimal_places=2,
                                verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 related_name='courses')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('category',)


class Teacher(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    specialty = models.CharField(max_length=255, verbose_name='Специальность')
    image = models.ImageField(upload_to='teacher', blank=True,
                              null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class CourseTeacher(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='teachers',
                               verbose_name='Курс')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,
                                related_name='courses',
                                verbose_name='Преподаватель')


class CourseImage(models.Model):
    image = models.ImageField(upload_to='course', verbose_name='Картинка',
                              null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='images', verbose_name='Курс')

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class CourseTopic(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    serial_number = models.IntegerField(verbose_name='Порядковый номер',
                                        null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='topics', verbose_name='Курс')

    class Meta:
        verbose_name = 'Лекция'
        verbose_name_plural = 'Лекции'
        ordering = ('serial_number',)

    def __str__(self):
        return self.title


class TopicLesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    serial_number = models.IntegerField(verbose_name='Порядковый номер',
                                        null=True)
    topic = models.ForeignKey(CourseTopic, on_delete=models.CASCADE,
                              related_name='lessons',
                              verbose_name='Лекция')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('serial_number',)

    def __str__(self):
        return self.title


class Rating(models.Model):
    RATING_RANGE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    created_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Время создания')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='rating', verbose_name='Курс')
    star = models.IntegerField(choices=RATING_RANGE,)
    user = models.ForeignKey(User, verbose_name='Пользователь',
                             related_name='rating',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.star}'


class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Время создания')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)

    def __str__(self):
        return f'{self.message}'


class Favorite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='favorites',
                               verbose_name='Курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites',
                             verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

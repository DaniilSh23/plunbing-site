from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ApplicationsTypes(models.Model):
    '''Модель вида заявок.
    На неё ссылается через FK модель Applications.'''
    LIST_FOR_CHOICES =[
        ('заказ', 'заказ'),
        ('консультация', 'консультация')
    ]
    applications_type = models.CharField(max_length=12, choices=LIST_FOR_CHOICES, verbose_name='Типы заявок')

    class Meta:
        db_table = 'Типы заявок'
        verbose_name = 'Типы заявок'
        verbose_name_plural = 'Типы заявок'

    def __str__(self):
        return self.applications_type


class Applications(models.Model):
    '''
    Модель заявок. Использует сторонний модуль PhoneNumberField для поля номера телефона.
    Связана FK с моделью "типы заявок".
    '''
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    text = models.TextField(max_length=1000)
    applications_type = models.ForeignKey(ApplicationsTypes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Заявки'
        verbose_name = 'Заявки'

    def __str__(self):
        return self.name


class Masters(models.Model):
    '''Модель мастеров'''
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=None, null=True)
    work_experience = models.FloatField(default=None, null=True)

    class Meta:
        db_table = 'Мастеры'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастеры'

    def __str__(self):
        return f'Мастер {self.name}'


class ImageForMasters(models.Model):
    '''Модель для загрузки файлов(фото) конкретной работы'''
    image = models.ImageField(upload_to='image_masters/%Y/%m/%d', null=True, blank=True)
    for_master = models.ForeignKey(Masters, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Фото мастеров'


class PriceList(models.Model):
    '''Модель прайс-лист'''
    works_title = models.CharField(max_length=1000)
    works_price = models.FloatField()

    class Meta:
        db_table = 'Прайс-лист'
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-листы'

    def __str__(self):
        return f'Прайс для {self.works_title}'


class Contacts(models.Model):
    '''Модель контактов владельцев'''
    name = models.CharField(max_length=50, verbose_name='Контактное лицо')
    phone_number = PhoneNumberField()
    email = models.EmailField()

    class Meta:
        db_table = 'Контакты'
        verbose_name = 'Контакты'

    def __str__(self):
        return f'Контакты {self.name}'


class OurWorks(models.Model):
    '''Модель для инфы о выполненных работах и фото к ним'''
    works_title = models.CharField(max_length=500, verbose_name='Название работы')
    works_price = models.FloatField(verbose_name='Цена работы')
    description = models.TextField(max_length=2000, verbose_name='Краткое описание работы')
    works_photo = models.ImageField(verbose_name='Фото работы')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'Наши работы'
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Наши работы'

    def __str__(self):
        return self.works_title


class PhotoForWorks(models.Model):
    '''Модель для загрузки фото конкретной работы'''

    file = models.ImageField(upload_to='files_works/%Y/%m/%d', null=True, blank=True, verbose_name='Фото работы')
    for_work = models.ForeignKey(OurWorks, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Фото работ'



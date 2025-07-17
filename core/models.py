from django.db import models

# Create your models here.
class Project(models.Model):
    company = models.CharField('Компания', max_length=255, unique=True)
    address = models.CharField('Адрес', max_length=255)
    text = models.CharField('Описание', max_length=512)
    photo1 = models.ImageField('Фото 1', upload_to='projects-photo/')
    photo2 = models.ImageField('Фото 2', upload_to='projects-photo/', null=True, blank=True)
    photo3 = models.ImageField('Фото 3', upload_to='projects-photo/', null=True, blank=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
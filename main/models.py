from django.db import models


# Create your models here.
class Client(models.Model):
    """Модель клиента для рассылки"""
    mail_client = models.CharField(max_length=25, verbose_name='Почта клиента для рассылки')
    name_client = models.CharField(max_length=20, verbose_name='Имя клиента')
    first_name_client = models.CharField(max_length=20, verbose_name='Фамилия клиента', null=True, blank=True)
    last_name_client = models.CharField(max_length=20, verbose_name='Отчество клиента', null=True, blank=True)

    def __str__(self):
        return f"Клиент:{self.name_client} {self.first_name_client} {self.last_name_client}.Письмо отправляем на {self.mail_client}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    """Модель рассылки, время, периодичность, статус"""
    FREQUENCY_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    STATUS_CHOICES = [
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    ]

    send_time = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='Периодичность рассылки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')

    def __str__(self):
        return f"Рассылка #{self.pk} время рассылки - {self.send_time} - {self.get_frequency_display()} - {self.get_status_display()}"

    class Meta:
        verbose_name_plural = "Рассылки"


class Message(models.Model):
    """Модель сообщения для рассылки """
    theme_mess = models.CharField(max_length=200, verbose_name='Тема письма')
    body_mess = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'Тема {self.theme_mess}, текст письма {self.body_mess}'

    class Meta:
        verbose_name_plural = "Сообщение для рассылки"


class MailingLogs(models.Model):
    """Модель логов рассылки"""
    mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE, verbose_name='Внешний ключ на рассылку')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=20, verbose_name='Cтатус попытки')
    server_response = models.TextField(blank=True, null=True, verbose_name='Ответ почтового сервера, если он был')

    def __str__(self):
        return f"Лог рассылки #{self.mailing.pk} - {self.timestamp} - {self.status}"

    class Meta:
        verbose_name_plural = "Логи рассылки"

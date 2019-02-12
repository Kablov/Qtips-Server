from django.db import models
from api.models import Profile
from datetime import datetime


class WithdrawRequest(models.Model):
    class Meta:
        verbose_name = 'Запрос на вывод средств'
        verbose_name_plural = 'Запросы на вывод средств'

    status = (
	('pending', 'На рассмотрении'),
	('paid', 'Выплачено'),
    ('declined', 'Отказано')
	)

    profile = models.ForeignKey(Profile, verbose_name = "Профиль", on_delete = models.DO_NOTHING)
    amount = models.DecimalField("Сумма", max_digits = 7, decimal_places = 2, default = 0.00)
    request_date = models.DateTimeField("Дата запроса", default = datetime.now)
    status = models.CharField("Статус", max_length = 8, choices = status, default = "pending")
    reviewed_time = models.DateTimeField("Время рассмотрения", default = datetime.now)

    def __str__(self):
        return str(self.id)

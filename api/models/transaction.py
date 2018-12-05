from django.db import models
from api.models import *
from datetime import datetime



class Transaction(models.Model):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    type = (
	('tip_payment', 'Оплата чаевых'),
	('withdrawal', 'Снятие со счета'),
	)

    to_user = models.ForeignKey(Profile, verbose_name = 'Кому', on_delete = models.DO_NOTHING)
    amount = models.DecimalField("Сумма", max_digits = 7, decimal_places = 2, default = 0.00)
    time = models.DateTimeField("Время", default = datetime.now)
    type = models.CharField("Тип транзакции", max_length = 11, choices = type, default = "tip_payment")

    def __str__(self):
        return str(self.id)

    def update_recipients_balance(self):
        profile = self.to_user
        transactions = Transaction.objects.filter(to_user = profile)
        profile.balance = sum(transaction.amount for transaction in transactions)
        profile.save(update_fields = ['balance'])

    def save(self, *args, **kwargs):
        models.Model.save(self, *args, **kwargs)
        self.update_recipients_balance()

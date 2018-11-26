from api.models import *
from qtips import settings
from qtips.exceptions import *


def is_user(request):
    if Token.objects.filter(token = request.META.get('HTTP_TOKEN')).count() == 0:
        raise AccessDenied("У вас нет прав для просмотра данной страницы")


def is_owner_or_read_only(request, profile):
    if Token.objects.filter(token = request.META.get('HTTP_TOKEN')).count() > 0:
        if Token.objects.get(token = request.META.get('HTTP_TOKEN')) != profile.token:
            raise AccessDenied("У вас нет прав для изменения данного профиля")
    else:
        raise AccessDenied("У вас нет прав для изменения данного профиля")


def access_key_check(request):
    if request.META.get('HTTP_ACCESS_KEY') != settings.ACCESS_KEY:
        print(request.META.get('HTTP_ACCESS_KEY'))
        raise AccessDenied("Доступ запрещен")

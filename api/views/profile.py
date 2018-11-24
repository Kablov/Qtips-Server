from django.db.models import Q
from django.shortcuts import render
from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from api.content import *
from qtips.exceptions import *
from qtips.permissions import *
import random


class SignUpView(APIView):
    def post(self, request, format = None):
        country_code = request.data['country_code']
        number = request.data['number']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        photo = request.data['photo']
        udid = request.data['udid']

        if udid == '':
            raise NoUdid("Нет udid")
        if country_code == '':
            raise CountryCodeNotEntered("Не введен код страны")
        if number == '':
            raise NumberNotEntered("Не введен номер")
        if first_name == '':
            raise FirstNameNotEntered("Не введено имя")
        if last_name == '':
            raise LastNameNotEntered("Не введена фамилия")

        phone = Phone.objects.get(Q(country_code = country_code) & Q(number = number))
        sms_code_udid = SmsCode.objects.get(phone = phone).udid

        if udid != sms_code_udid:
            raise UdidsDoNotMatch("Введеный udid не совпадает с записанным в базе данных")

        if Profile.objects.filter(phone = phone).count() == 0:
            profile = Profile()
            profile.phone = phone
            profile.first_name = first_name
            profile.last_name = last_name
            if photo:
                profile.photo = upload_photo(photo, phone)
            else:
                profile.photo = ''
            profile.save()
            token = Token()
            token.profile = profile
            token.save()
        else:
            raise ProfileEngaged("Аккаунт с указанным номером телефона уже существует")

        token = profile.token.token
        result = {
            'token': token
        }
        return Response(result, status = status.HTTP_201_CREATED)


class ProfilePageView(APIView):

    def get(self, request, id, format = None):
        is_user(request)
        profile = Profile.objects.get(external_id = id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, id, format = None):
        profile = Profile.objects.get(external_id = id)
        is_owner_or_read_only(request, profile)
        profile = Profile.objects.filter(external_id = id)

        if 'first_name' in request.data:
            new_first_name = request.data['first_name']
            profile.update(first_name = new_first_name)

        if 'last_name' in request.data:
            new_last_name = request.data['last_name']
            profile.update(last_name = new_last_name)

        if 'photo' in request.data:
            new_photo = request.data['photo']
            profile.update(photo = new_photo)

        serializer = ProfileSerializer(profile, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

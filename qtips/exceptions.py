class VerboseException(Exception):
    code = 0
    verbose_msg = "Сообщение отсутствует"

    def get_verbose(self):
        return self.verbose_msg.capitalize()

    def get_code(self):
        return self.code


class ProfileEngaged(VerboseException):
    code = 102
    verbose_msg = "Аккаунт с указанным номером телефона уже существует"


class CodesDoNotMatch(VerboseException):
    code = 105
    verbose_msg = "Коды не совпадают"


class AccessDenied(VerboseException):
    code = 108
    verbose_msg = "Доступ запрещен"


class CodeNotSent(VerboseException):
    code = 109
    verbose_msg = "Не удалось отправить код подтверждения"

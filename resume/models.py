from django.db import models


class Profile(models.Model):
    full_name = models.CharField("Имя", max_length=100)
    about_text = models.TextField("Текст резюме", blank=True)
    avatar = models.ImageField("Фото", upload_to="profile/", blank=True, null=True)

    qualification = models.CharField("Квалификация", max_length=150, blank=True)
    hobbies = models.CharField("Хобби", max_length=200, blank=True)

    # справа (языки по звёздам, как на фотке)
    language_1 = models.CharField("Язык 1", max_length=50, blank=True)
    language_1_stars = models.IntegerField("Звёзды 1", default=5)

    language_2 = models.CharField("Язык 2", max_length=50, blank=True)
    language_2_stars = models.IntegerField("Звёзды 2", default=4)

    language_3 = models.CharField("Язык 3", max_length=50, blank=True)
    language_3_stars = models.IntegerField("Звёзды 3", default=3)

    def __str__(self):
        return self.full_name


class LeftBlock(models.Model):
    """
    Это то что меняется в зелёной части:
    резюме / поддержка / и т.д.
    """
    key = models.CharField("Ключ", max_length=50, unique=True)  # resume, support, plans, skills ...
    title = models.CharField("Заголовок", max_length=100)
    content = models.TextField("Текст", blank=True)

    # ссылки (для поддержки)
    instagram = models.CharField("Instagram", max_length=200, blank=True)
    telegram = models.CharField("Telegram", max_length=200, blank=True)

    def __str__(self):
        return self.key


class AdminUser(models.Model):
    """
    Твоя простая админка (логин/пароль).
    """
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)  # (можно потом хешировать)

    def __str__(self):
        return self.username
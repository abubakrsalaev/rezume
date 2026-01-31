from django.db import models


class Profile(models.Model):
    full_name = models.CharField("Имя", max_length=120)
    position = models.CharField("Должность", max_length=120, blank=True)
    about = models.TextField("Обо мне", blank=True)

    photo = models.ImageField("Фото", upload_to="profile/", blank=True, null=True)

    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=50, blank=True)
    location = models.CharField("Город", max_length=120, blank=True)

    instagram = models.URLField("Instagram", blank=True)
    telegram = models.URLField("Telegram", blank=True)
    github = models.URLField("GitHub", blank=True)

    resume_text = models.TextField("Резюме (текст)", blank=True)
    portfolio_text = models.TextField("Портфолио (текст)", blank=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField("Навык", max_length=120)

    def __str__(self):
        return self.name


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    title = models.CharField("Должность", max_length=120)
    company = models.CharField("Компания", max_length=120, blank=True)
    years = models.CharField("Годы", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.title} ({self.company})"


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="educations")
    name = models.CharField("Учёба / Университет", max_length=200)
    years = models.CharField("Годы", max_length=50, blank=True)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        return self.name
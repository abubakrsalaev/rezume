from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile, LeftBlock, AdminUser
from .serializers import ProfileSerializer, LeftBlockSerializer


# ---------------- helpers ----------------

def get_profile():
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(
            full_name="Ваше имя",
            about_text="Заполни через админку",
            qualification="",
            hobbies="",
            language_1="Русский",
            language_1_stars=5,
            language_2="Английский",
            language_2_stars=4,
            language_3="",
            language_3_stars=0,
        )
    return profile


def get_left_block(key: str):
    block = LeftBlock.objects.filter(key=key).first()
    if not block:
        block = LeftBlock.objects.create(
            key=key,
            title="Раздел",
            content="Заполни через админку",
            instagram="",
            telegram="",
        )
    return block


# ---------------- WEB ----------------

def index(request):
    profile = get_profile()
    left_block = get_left_block("resume")

    return render(request, "resume/index.html", {
        "profile": profile,
        "left_block": left_block,
    })


def login_page(request):
    return render(request, "resume/login.html")


@csrf_exempt
def login_post(request):
    """
    Вход работает:
    1) через Django superuser (createsuperuser)
    2) через твою модель AdminUser
    """
    if request.method != "POST":
        return redirect("/login/")

    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "").strip()

    # 1) Django superuser
    user = authenticate(username=username, password=password)
    if user and user.is_superuser:
        request.session["admin_id"] = f"django_{user.id}"
        return redirect("/admin-panel/")

    # 2) AdminUser
    admin_user = AdminUser.objects.filter(username=username, password=password).first()
    if admin_user:
        request.session["admin_id"] = f"custom_{admin_user.id}"
        return redirect("/admin-panel/")

    return render(request, "resume/login.html", {"error": "Неверный логин или пароль"})


def logout_view(request):
    request.session.flush()
    return redirect("/")


def admin_panel(request):
    if not request.session.get("admin_id"):
        return redirect("/login/")

    profile = get_profile()
    blocks = LeftBlock.objects.all().order_by("key")

    # если нет нужных блоков — создадим автоматически
    for key, title in [
        ("resume", "Резюме"),
        ("plans", "Планы"),
        ("skills", "Навыки"),
        ("support", "Поддержка"),
    ]:
        LeftBlock.objects.get_or_create(key=key, defaults={"title": title, "content": ""})

    blocks = LeftBlock.objects.all().order_by("key")

    return render(request, "resume/admin_panel.html", {
        "profile": profile,
        "blocks": blocks
    })


@csrf_exempt
def admin_save(request):
    if not request.session.get("admin_id"):
        return JsonResponse({"ok": False, "error": "Нет доступа"}, status=403)

    if request.method != "POST":
        return JsonResponse({"ok": False, "error": "Только POST"}, status=405)

    profile = get_profile()

    # профиль
    profile.full_name = request.POST.get("full_name", profile.full_name)
    profile.about_text = request.POST.get("about_text", profile.about_text)
    profile.qualification = request.POST.get("qualification", profile.qualification)
    profile.hobbies = request.POST.get("hobbies", profile.hobbies)

    profile.language_1 = request.POST.get("language_1", profile.language_1)
    profile.language_1_stars = int(request.POST.get("language_1_stars", profile.language_1_stars) or 0)

    profile.language_2 = request.POST.get("language_2", profile.language_2)
    profile.language_2_stars = int(request.POST.get("language_2_stars", profile.language_2_stars) or 0)

    profile.language_3 = request.POST.get("language_3", profile.language_3)
    profile.language_3_stars = int(request.POST.get("language_3_stars", profile.language_3_stars) or 0)

    if "avatar" in request.FILES:
        profile.avatar = request.FILES["avatar"]

    profile.save()

    # блоки слева
    keys = request.POST.getlist("block_key")
    titles = request.POST.getlist("block_title")
    contents = request.POST.getlist("block_content")
    instas = request.POST.getlist("block_instagram")
    teles = request.POST.getlist("block_telegram")

    for i in range(len(keys)):
        b = LeftBlock.objects.filter(key=keys[i]).first()
        if not b:
            b = LeftBlock.objects.create(key=keys[i], title=titles[i], content=contents[i])

        b.title = titles[i]
        b.content = contents[i]
        b.instagram = instas[i]
        b.telegram = teles[i]
        b.save()

    return JsonResponse({"ok": True})


# ---------------- API ----------------

@api_view(["GET"])
def api_profile(request):
    profile = get_profile()
    return Response(ProfileSerializer(profile).data)


@api_view(["GET"])
def api_left_block(request, key):
    block = get_left_block(key)
    return Response(LeftBlockSerializer(block).data)
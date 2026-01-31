from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Skill, Experience, Education


def index(request):
    profile = Profile.objects.first()
    return render(request, "resume/index.html", {"profile": profile})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("resume:admin_panel")

    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("resume:admin_panel")
        else:
            error = "Неверный логин или пароль"

    return render(request, "resume/login.html", {"error": error})


@login_required
def logout_view(request):
    logout(request)
    return redirect("resume:index")


@login_required
def admin_dashboard(request):
    profile = Profile.objects.first()
    return render(request, "resume/admin/login.html", {"profile": profile})


# -------------------- PROFILE --------------------
@login_required
def admin_profile(request):
    profile = Profile.objects.first()

    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name", "")
        profile.position = request.POST.get("position", "")
        profile.about = request.POST.get("about", "")
        profile.location = request.POST.get("location", "")

        if "photo" in request.FILES:
            profile.photo = request.FILES["photo"]

        profile.save()
        return redirect("resume:admin_profile")

    return render(request, "resume/admin/profile.html", {"profile": profile})


# -------------------- CONTACTS --------------------
@login_required
def admin_contacts(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        profile.phone = request.POST.get("phone", "")
        profile.email = request.POST.get("email", "")
        profile.save()
        return redirect("resume:admin_contacts")

    return render(request, "resume/admin/contacts.html", {"profile": profile})


# -------------------- SOCIALS --------------------
@login_required
def admin_socials(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        profile.instagram = request.POST.get("instagram", "")
        profile.telegram = request.POST.get("telegram", "")
        profile.github = request.POST.get("github", "")
        profile.save()
        return redirect("resume:admin_socials")

    return render(request, "resume/admin/socials.html", {"profile": profile})


# -------------------- RESUME TEXT --------------------
@login_required
def admin_resume(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        profile.resume_text = request.POST.get("resume_text", "")
        profile.save()
        return redirect("resume:admin_resume")

    return render(request, "resume/admin/resume.html", {"profile": profile})


# -------------------- PORTFOLIO TEXT --------------------
@login_required
def admin_portfolio(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        profile.portfolio_text = request.POST.get("portfolio_text", "")
        profile.save()
        return redirect("resume:admin_portfolio")

    return render(request, "resume/admin/portfolio.html", {"profile": profile})


# -------------------- SKILLS --------------------
@login_required
def admin_skills(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            Skill.objects.create(profile=profile, name=name)
        return redirect("resume:admin_skills")

    skills = profile.skills.all()
    return render(request, "resume/admin/skills.html", {"profile": profile, "skills": skills})


@login_required
def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    skill.delete()
    return redirect("resume:admin_skills")


# -------------------- EXPERIENCE --------------------
@login_required
def admin_experience(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        Experience.objects.create(
            profile=profile,
            title=request.POST.get("title", ""),
            company=request.POST.get("company", ""),
            years=request.POST.get("years", ""),
            description=request.POST.get("description", ""),
        )
        return redirect("resume:admin_experience")

    items = profile.experiences.all()
    return render(request, "resume/admin/experience.html", {"profile": profile, "items": items})


@login_required
def delete_experience(request, exp_id):
    item = get_object_or_404(Experience, id=exp_id)
    item.delete()
    return redirect("resume:admin_experience")


# -------------------- EDUCATION --------------------
@login_required
def admin_education(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Моё имя")

    if request.method == "POST":
        Education.objects.create(
            profile=profile,
            name=request.POST.get("name", ""),
            years=request.POST.get("years", ""),
            description=request.POST.get("description", ""),
        )
        return redirect("resume:admin_education")

    items = profile.educations.all()
    return render(request, "resume/admin/education.html", {"profile": profile, "items": items})


@login_required
def delete_education(request, edu_id):
    item = get_object_or_404(Education, id=edu_id)
    item.delete()
    return redirect("resume:admin_education")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile

@login_required
def admin_panel(request):
    profile = Profile.objects.first()
    if not profile:
        profile = Profile.objects.create(full_name="Ваше имя")

    if request.method == "POST":
        profile.full_name = request.POST.get("full_name", "")
        profile.position = request.POST.get("position", "")
        profile.phone = request.POST.get("phone", "")
        profile.email = request.POST.get("email", "")

        profile.instagram = request.POST.get("instagram", "")
        profile.telegram = request.POST.get("telegram", "")
        profile.github = request.POST.get("github", "")

        profile.about = request.POST.get("about", "")
        profile.resume_text = request.POST.get("resume_text", "")
        profile.portfolio_text = request.POST.get("portfolio_text", "")

        if "photo" in request.FILES:
            profile.photo = request.FILES["photo"]

        profile.save()
        return redirect("resume:admin_panel")

    return render(request, "resume/admin_panel.html", {"profile": profile})
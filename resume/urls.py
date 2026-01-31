from django.urls import path
from . import views

app_name = "resume"

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("admin/", views.admin_dashboard, name="admin_dashboard"),

    path("admin/profile/", views.admin_profile, name="admin_profile"),
    path("admin/contacts/", views.admin_contacts, name="admin_contacts"),
    path("admin/socials/", views.admin_socials, name="admin_socials"),
    path("admin/resume/", views.admin_resume, name="admin_resume"),
    path("admin/portfolio/", views.admin_portfolio, name="admin_portfolio"),

    path("admin/skills/", views.admin_skills, name="admin_skills"),
    path("admin/skills/delete/<int:skill_id>/", views.delete_skill, name="delete_skill"),

    path("admin/experience/", views.admin_experience, name="admin_experience"),
    path("admin/experience/delete/<int:exp_id>/", views.delete_experience, name="delete_experience"),

    path("admin/education/", views.admin_education, name="admin_education"),
    path("admin/education/delete/<int:edu_id>/", views.delete_education, name="delete_education"),
    path("admin-panel/", views.admin_panel, name="admin_panel"),
    path("accounts/login/", views.login_view, name="login"),

]
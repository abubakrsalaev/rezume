from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login/", views.login_page),
    path("login/post/", views.login_post),
    path("logout/", views.logout_view),

    path("admin-panel/", views.admin_panel),
    path("admin-save/", views.admin_save),

    path("api/profile/", views.api_profile),
    path("api/left/<str:key>/", views.api_left_block),
]
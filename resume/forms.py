from django import forms
from .models import Profile, Skill, Project, Language

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = "__all__"
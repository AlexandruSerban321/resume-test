from django.shortcuts import render
from .models import Education, Experience, Category_skill, Skill, Interests
# Create your views here.
def index(request):
    all_educations = Education.objects.order_by("-id")
    all_experiences = Experience.objects.order_by("-id")
    all_categories_skills = Category_skill.objects.order_by()
    all_skill = Skill.objects.order_by()
    all_interests = Interests.objects.order_by()
    context = {
        "all_educations": all_educations,
        "all_experiences": all_experiences,
        "all_categories_skills": all_categories_skills,
        "all_skill": all_skill,
        "all_interests": all_interests,
    }
    return render(request, 'base.html', context)
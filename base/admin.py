from django.contrib import admin
from .models import Education, Experience, Category_skill, Skill, Interests

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Interests)
admin.site.register(Category_skill)
from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    field = models.CharField(max_length=50, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.institution

class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.company

class Category_skill(models.Model):
    class Meta:
        verbose_name_plural = 'categories_skills'
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(
        'Category_skill', on_delete=models.SET_NULL, blank=True, null=True
    )
    skill = models.CharField(max_length=50)
    progresbar = models.IntegerField(default=0)
    def __str__(self):
        return self.skill

class Interests(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=30)
    def __str__(self):
        return self.name
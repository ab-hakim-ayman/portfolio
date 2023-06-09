from django.contrib import admin

from .models import(
    About, Education, Experience,
     Skill, Service, Category, Project,
    Testimonial, Social, Contact,
    Achievement,
)

# Register your models here.
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Social)
admin.site.register(Contact)
admin.site.register(Achievement)
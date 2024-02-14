from django.contrib import admin
from .models import (
    services,
    Team,
    Testimonials,
    Category,
    protfolio,
    contact,
  
)
# Register your models here.
class serviceAdmin(admin.ModelAdmin):
    pass
admin.site.register(services, serviceAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Team,TeamAdmin)

class TestimonialsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Testimonials, TestimonialsAdmin)

class categoryAdmin(admin.ModelAdmin):
   pass
admin.site.register(Category,categoryAdmin)

class portfolioAdmin(admin.ModelAdmin):
   pass
admin.site.register(protfolio,portfolioAdmin)
admin.site.register(contact)

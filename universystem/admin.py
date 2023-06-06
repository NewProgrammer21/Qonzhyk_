from django.contrib import admin
from .models import Profile, Roles, Course, Lesson, EnrollCource, Message, SRP,Comment,laboratorywork

admin.site.register(Profile)
admin.site.register(Roles)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(laboratorywork)
admin.site.register(Message)

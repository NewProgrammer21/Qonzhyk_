from django import template
from universystem.models import Lesson, Profile
register = template.Library()


@register.simple_tag()
def leson_count_all():
    return Lesson.objects.all().count()

@register.simple_tag()
def teacher_count_all():
    return Profile.objects.filter(roles=1).count()


@register.simple_tag()
def student_count_all():
    return Profile.objects.filter(roles=2).count()
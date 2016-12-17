


from django.contrib import admin

# Register your models here.
from adminsortable2.admin import SortableAdminMixin

from .models import Question

class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
admin.site.register(Question,QuestionAdmin)




from django.contrib import admin

# Register your models here.
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminMixin

# from .models import Question, User, Person

from .models import Author,Book,Membership

class MembershipInline(SortableInlineAdminMixin,admin.TabularInline): #SortableInlineAdminMixin
	model = Membership
	readonly_fields = ['author',]	
	


class BookAdmin(SortableAdminMixin,admin.ModelAdmin):
	inlines = (MembershipInline,)	
		
		
class AuthorAdmin(SortableAdminMixin,admin.ModelAdmin):

	inlines = (MembershipInline,)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)



# Reference: http://stackoverflow.com/questions/21562645/django-many-to-many-inline-how-to-show-fields-referenced-by-through-model
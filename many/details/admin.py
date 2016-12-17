


from django.contrib import admin

# Register your models here.
from adminsortable2.admin import SortableInlineAdminMixin,SortableAdminMixin

# from .models import Question, User, Person

from .models import Author,Book,Membership

class MembershipInline(SortableInlineAdminMixin,admin.TabularInline): #
	model = Membership
	# fields = ('book','author',)

# class AuthorInline(SortableInlineAdminMixin,admin.TabularInline):
# 	model = Author #Book.authors.through
# 	inlines = (MembershipInline,)


class MembershipAdmin(SortableAdminMixin,admin.ModelAdmin):
	pass


class BookAdmin(SortableAdminMixin,admin.ModelAdmin):
	list_display = ('title',)
	inlines = (MembershipInline,)
	# exclude = ('book',)
		
		
class AuthorAdmin(SortableAdminMixin,admin.ModelAdmin):
	# pass
	list_display = ('name',)
	# inlines = (MembershipInline,)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Membership,MembershipAdmin)
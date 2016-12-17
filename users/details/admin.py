


from django.contrib import admin

# Register your models here.
from adminsortable2.admin import SortableInlineAdminMixin

# from .models import Question, User, Person

from .models import Author,Book

# class QuestionAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass
# #admin.site.register(Question,QuestionAdmin)

# class UserInline(admin.TabularInline):
#     model = User
#     extra = 2 # how many rows to show

# class PersonAdmin(admin.ModelAdmin):
#     inlines = (UserInline,)

class AuthorInline(SortableInlineAdminMixin,admin.TabularInline):
	model = Book.authors.through
	# list_display_links = ('author',)
	# list_display = ('author',)
	extra = 1

# class AuthorInline(admin.TabularInline):
# 	model = Book.authors.through

class BookAdmin(admin.ModelAdmin):
	# list_display = ('title',)
	inlines = (AuthorInline,)
		
		
class AuthorAdmin(admin.ModelAdmin):
	inlines = (AuthorInline,)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)



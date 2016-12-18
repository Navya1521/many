

from django.shortcuts import render

from django.http import HttpResponse

from .models import Author, Book, Membership


def index(request):
	# author_name = Author.objects.get(name = request.author.name)
	# Membership.author = author_name
	# book = Book.objects.get(title = request.book.title)
	# Membership.book = book

	# Membership.save()
	return HttpResponse("Hello, world. You're at the polls index.")




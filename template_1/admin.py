from django.contrib import admin
from .models import books,firstpage_main_book_of_week,firstpage_mainbackground,firstpage_news,firstpage_famous_novelist,review
# Register your models here.

class choiceline(admin.StackedInline):
    model = review
    extra = 1

class bookadmin(admin.ModelAdmin):
    fieldsets = [
        ('BOOK INFORMATION',{'fields':['id','book_name','book_image','book_description','book_file','total_pages','total_chapter','awards']}),
        ('AUTHOR INFORMATION',{'fields':['book_author','author_image','author_descriptions']})


    ]
    inlines = [choiceline]

admin.site.register(firstpage_mainbackground)
admin.site.register(firstpage_main_book_of_week)
admin.site.register(books,bookadmin)
admin.site.register(firstpage_famous_novelist)
admin.site.register(firstpage_news)
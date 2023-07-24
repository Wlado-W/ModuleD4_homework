# Register your models here.
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_formatted_date', 'get_short_text', 'author')

    def get_short_text(self, obj):
        return obj.get_short_text()
    get_short_text.short_description = 'Текст статьи'

    def get_formatted_date(self, obj):
        return obj.get_formatted_date()
    get_formatted_date.short_description = 'Дата публикации'

admin.site.register(News, NewsAdmin)


from django.contrib import admin

from .models import *

# class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline): #表格形式
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10

    # fields=['bpub_date','btitle'] #属性的先后顺序
    fieldsets = [
        ('basic',{'fields':['btitle']}),
        ('more',{'fields':['bpub_date']})
    ] #属性先后顺序并且可以分组

    inlines = [HeroInfoInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
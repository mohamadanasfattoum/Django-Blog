from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post , Comment


class PostAdmin(SummernoteModelAdmin):
    list_display = ['title' , 'publish_date']
    summernote_fields = '__all__'

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
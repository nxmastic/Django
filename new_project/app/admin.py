from django.contrib import admin
from .models import Board, Comment
#앱에 있는 db를 등록하게 해주는거
# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)
from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 5
    min_num = 3
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display =('id', 'image', 'content', 'created_at', 'view_count', 'writer')
    #list_editable = ('content',)
    list_filter = ('created_at',)
    search_fields = ('id','writer__username',)
    search_help_text = '게시판 및 작성자 검색이 가능합니다'
    inlines = [CommentInLine]
    readonly_fields = ('created_at',)

#admin.site.register(Comment)
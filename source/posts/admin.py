from django.contrib import admin

# Register your models here.
from .models import Post,Author,Category,Comment,PostView

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)
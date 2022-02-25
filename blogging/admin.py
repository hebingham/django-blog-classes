# blogging/admin.py

from django.contrib import admin

from blogging.models import Post, Category


class InlineModelAdmin(admin.TabularInline):
    model = Category.posts.through
    # model = Category


class PostAdmin(admin.ModelAdmin):
    inlines = [InlineModelAdmin,]


class CategoryAdmin(admin.ModelAdmin):
    # inlines = [
        # InlineModelAdmin,
    # ]
    exclude = ('posts',)


# admin.site.register(Post)
# admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
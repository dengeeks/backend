from django.contrib import admin

from topic_pdd.models import Topic, Heading


# Register your models here.

class HeadingAdmin(admin.StackedInline):
    model = Heading


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    inlines = (HeadingAdmin,)


@admin.register(Heading)
class HeadingAdmin(admin.ModelAdmin):
    pass

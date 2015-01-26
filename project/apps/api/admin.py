from django.contrib import admin

from .models import (
    Singer,
    Chorus,
    Quartet,
    District,
    Chapter,
    Contest,
    QuartetPerformance,
    ChorusPerformance,
)


class ChorusPerformanceInline(admin.TabularInline):
    model = ChorusPerformance


class QuartetPerformanceInline(admin.TabularInline):
    model = QuartetPerformance
    fields = (
        'quartet',
        'round',
        'queue',
        'song1',
        'song2',
    )


class CommonAdmin(admin.ModelAdmin):
    search_fields = ['name']
    save_on_top = True


@admin.register(Singer)
class SingerAdmin(CommonAdmin):
    pass


@admin.register(District)
class DistrictAdmin(CommonAdmin):
    pass


@admin.register(Chapter)
class ChatperAdmin(CommonAdmin):
    pass


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    inlines = [
        QuartetPerformanceInline,
    ]
    save_on_top = True


@admin.register(Quartet)
class QuartetAdmin(CommonAdmin):
    inlines = [
        QuartetPerformanceInline,
    ]


@admin.register(Chorus)
class ChorusAdmin(CommonAdmin):
    inlines = [
        ChorusPerformanceInline,
    ]


@admin.register(QuartetPerformance)
class QuartetPerformanceAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(ChorusPerformance)
class ChorusPerformanceAdmin(admin.ModelAdmin):
    save_on_top = True

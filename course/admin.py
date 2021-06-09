from django.contrib import admin
from .models import (Company, Contact, Rating, SocialMedia,
                     Category, Teacher, CourseImage,
                     Course, CourseTopic, TopicLesson,
                     Star, CourseTeacher, Rating)


class AdContactInline(admin.TabularInline):
    model = Contact
    fields = ('phone_number',)
    max_num = 10
    min_num = 1
    extra = 1


class AdMediaInline(admin.TabularInline):
    model = SocialMedia
    fields = ('media_name', 'url')
    max_num = 10
    min_num = 1
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    inlines = (AdContactInline, AdMediaInline,)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('media', 'url')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


class AdTeacherInline(admin.TabularInline):
    model = CourseTeacher
    extra = 1


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty')
    inlines = (AdTeacherInline,)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'category')
    inlines = (AdTeacherInline,)


@admin.register(CourseImage)
class CourseImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'course')


class AdLessonInline(admin.TabularInline):
    model = TopicLesson
    fields = ('title', 'serial_number')
    max_num = 30
    min_num = 1


@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'serial_number')
    inlines = [AdLessonInline,]


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'course', 'user')
from django.contrib import admin
from .models import (Company, Contact, SocialMedia,
                     Category, Teacher, CourseImage,
                     Course, CourseTopic, TopicLesson,
                     Star)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('media', 'url')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty', 'course')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'category')


@admin.register(CourseImage)
class CourseImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'course')


@admin.register(CourseTopic)
class CourseTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'serial_number')


@admin.register(TopicLesson)
class TopicLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'serial_number')


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('value',)


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('star', 'course')
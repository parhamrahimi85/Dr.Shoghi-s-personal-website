from django.contrib import admin
from .models import Vars, Customer, Skills, ComImages, UserRequest, Job, Blog

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline


def translation_admin_media():
    return {
        'js': (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        ),
        'css': {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        },
    }


class CustomerInline(TranslationStackedInline):
    model = Customer
    extra = 1


@admin.register(Vars)
class VariablesAdmin(TranslationAdmin):
    inlines = [CustomerInline]

    class Media:
        js = translation_admin_media()['js']
        css = translation_admin_media()['css']


@admin.register(Skills)
class SkillAdmin(TranslationAdmin):
    class Media:
        js = translation_admin_media()['js']
        css = translation_admin_media()['css']


@admin.register(Job)
class SkillAdmin(TranslationAdmin):
    class Media:
        js = translation_admin_media()['js']
        css = translation_admin_media()['css']


@admin.register(Blog)
class SkillAdmin(TranslationAdmin):
    class Media:
        js = translation_admin_media()['js']
        css = translation_admin_media()['css']


@admin.register(ComImages)
class UserInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRequest)
class UserInfoAdmin(admin.ModelAdmin):
    pass


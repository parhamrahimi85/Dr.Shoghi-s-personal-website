from .models import Vars, Skills, Customer, Job, Blog

from modeltranslation.translator import TranslationOptions, register


@register(Vars)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'aboutme',
        'name1',
        'name2',
        'name3',
        'what_can_i_do_title1',
        'wcid_des1',
        'what_can_i_do_title2',
        'wcid_des2',
        'what_can_i_do_title3',
        'wcid_des3',
        'aboutme_title',
        'aboutme_des',
        'address',
        'sub_des1',
        'sub_des2',
        'sub_des3',

    )


@register(Skills)
class PhotoTranslationOptions(TranslationOptions):
    fields = (
        "Skill",
    )


@register(Customer)
class PhotoTranslationOptions(TranslationOptions):
    fields = (
        "name",
        'des',
        'Customer_opinion'
    )


@register(Job)
class PhotoTranslationOptions(TranslationOptions):
    fields = (
        "title",
        'des',
    )


@register(Blog)
class PhotoTranslationOptions(TranslationOptions):
    fields = (
        "blog_title",
        'des',
        'sub_des',
    )

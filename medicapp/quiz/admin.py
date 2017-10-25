from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['question']}),
        ('Choices',    {'fields': ['choice_text', 'correct_answer']}),
    ]

    list_display = ('question', 'choice_text', 'correct_answer')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
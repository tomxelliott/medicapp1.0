from django.contrib import admin

from .models import Topic, Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    max_num = 4


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['topic_text']}),
    ]
    search_fields = ['topic_text']


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('TOPIC',   {'fields': ['topic']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['question']}),
        ('Choices',    {'fields': ['choice_text', 'correct_answer']}),
    ]

    list_display = ('question', 'choice_text', 'correct_answer')
    # Remove if the filtering of answers is deemed unnecessary.
    list_filter = ['correct_answer']
    search_fields = ['choice_text']


admin.site.register(Topic, TopicAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
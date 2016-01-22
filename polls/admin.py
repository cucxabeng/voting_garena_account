from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',   {'fields': ['question_title']}),
        ('Content', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
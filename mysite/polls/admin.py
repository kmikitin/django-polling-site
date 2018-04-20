from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# This tells Django that choice objects are edited on the amin page. 
# By default, provide enough fields for 3 choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Here is where we set the Choices, they'll be registered with the Question model
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
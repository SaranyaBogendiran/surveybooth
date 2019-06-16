from django.contrib import admin

# Register your models here.
from surveyhome.models import SurveyType, Logo, QuestionType, Questionarie, SurveyTitle, ResponseCollector, UserProfile, UserProfileForm

#Define Inline class
class QuestionarieInline(admin.TabularInline):
    model = Questionarie

class ResponseCollectorInline(admin.TabularInline):
    model = ResponseCollector

#Define Admin class

class SurveyTitleAdmin(admin.ModelAdmin):
    list_display = ('title','surveytype','logo','username')
    fields = ['title','surveytype','logo','username']
    inlines = [QuestionarieInline,ResponseCollectorInline]

# Register the models
admin.site.register(Logo)
admin.site.register(SurveyType)
admin.site.register(QuestionType)
admin.site.register(Questionarie)
admin.site.register(SurveyTitle, SurveyTitleAdmin)

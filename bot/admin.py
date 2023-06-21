from django.contrib import admin
from bot.models import (
    Member,
    Report,
    Question,
    Event,

)
from django.utils.translation import gettext_lazy as _
# import logging
#
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s', level=logging.DEBUG,
# )
#
# logger = logging.getLogger(__name__)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'chat_id',
        'name',
    )


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'speaker',
    )    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'speakers':
            kwargs['queryset'] = Member.objects.filter(is_speaker=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Event, EventAdmin)
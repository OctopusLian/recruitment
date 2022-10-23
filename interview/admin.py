from django.contrib import admin

from interview.models import Candidate

# Register your models here.
# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    # 不需要展示的字段
    exclude = ('creator', 'created_date', 'modified_date')
    # 需要展示的字段
    list_display = (
        'username', 'city', 'bachelor_school', 'first_score', 'first_result','first_interviewer_user',
        'second_score','second_result', 'second_interviewer_user','hr_score', 'hr_result','hr_interviewer_user',
        'last_editor',
    )

admin.site.register(Candidate,CandidateAdmin)
from django.contrib import admin

from interview.models import Candidate

# Register your models here.
# 候选人管理类
class CandidateAdmin(admin.ModelAdmin):
    # 不需要展示的字段
    exclude = ('creator', 'created_date', 'modified_date')
    # 需要展示的字段
    list_display = (
        'username', 'city', 'bachelor_school', 'get_resume', 'first_score', 'first_result',
        'second_score','second_result', 'hr_score', 'hr_result',
        'last_editor',
    )

admin.site.register(Candidate,CandidateAdmin)
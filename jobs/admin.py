from django.contrib import admin
from jobs.models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    # 隐藏字段，让系统自动生成
    exclude = ('creator','created_date','modified_date')
    # 页面上展示的字段
    list_display = ('job_name', 'job_type', 'job_city', 'creator', 'created_date', 'modified_date')

    def save_model(self, request, obj, form, change):
        if obj.creator is None:
            obj.creator = request.user
            # 调用父类方法
        super().save_model(request, obj, form, change)

admin.site.register(Job,JobAdmin)
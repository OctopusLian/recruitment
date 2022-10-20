from django.db import models

# Create your models here.

JobTypes = [
    (0, "技术类"),
    (1, "产品类"),
    (2, "运营类"),
    (3, "设计类"),
    (4, "市场营销类")
]

class Job(models.Model):
    # 不允许为空
    job_type = models.SmallIntegerField(blank=False,choices=JobTypes,verbose_name="职位类型")
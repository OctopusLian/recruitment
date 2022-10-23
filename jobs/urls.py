from django.urls import path
from jobs import views

urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
    # 职位详情
    #url(r'^job/(?P<job_id>\d+)/$', views.detail, name='detail'),
    path('job/<int:job_id>/', views.detail, name='detail'),
]
# 基于Django框架的招聘网站  

- Django 4.1.2  
- Python 3.8.10

## 运行  

### 超级管理员  

http://127.0.0.1:8000/admin/  
账号：admin  
邮箱：a@qq.com  
密码：123456  


## 常用操作  

```
# 运行
python manage.py runserver

# 同步表
python manage.py makemigrations

# 使改动生效
python manage.py migrate

# 创建应用
python manage.py startapp <应用名称>

# 导入csv文件
python manage.py import_candidates --path candidates.csv
```
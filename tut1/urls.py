
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stu/',views.StudenntsView,name='stu'),
    path('stu/',views.student_api,name='stu'),
    path('stu/<int:pk>',views.student_api,name='stu'),
]

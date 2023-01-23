from django.contrib import admin
from student_management.models import Student_Details
@admin.register(Student_Details)
class Student_Details_admin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','branch','email','password','score','phone')
    search_fields=('first_name',)
    list_filter=('last_name',)
    list_per_page=10

# Register your models here.

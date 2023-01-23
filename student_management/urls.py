from student_management import views
from django.urls import path

urlpatterns = [
    path('post/',views.post),
    path('delete/<int:id>/',views.delete),
    path('update/<int:id>/',views.update),
    path('get/',views.get),
]

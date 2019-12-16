from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    CourseCreateView,
    # my_fbv
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', my_fbv, name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name="course-detail'"),
    path('create/', CourseCreateView.as_view(), name="course-create"),
]

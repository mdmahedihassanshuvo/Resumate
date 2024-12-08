from django.urls import path

# from local imports
from .views import StudentView


urlpatterns = [
    path('student/', StudentView.as_view(), name='student_list'),
]

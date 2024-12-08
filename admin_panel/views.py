from django.views.generic import TemplateView

# from local imports
from .models import Student


class StudentView(TemplateView):
    model = Student
    template_name = 'admin_panel/student.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.all()

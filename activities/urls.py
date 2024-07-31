from django.urls import path
from .views import index, type_step, subject_step, year_step, cost_step, effort_step, extracurricular_detail

urlpatterns = [
    path('', index, name='index'),
    path('type/', type_step, name='type_step'),
    path('subject/', subject_step, name='subject_step'),
    path('year/', year_step, name='year_step'),
    path('cost/', cost_step, name='cost_step'),
    path('effort/', effort_step, name='effort_step'),
    path('<int:extracurricular_id>/', extracurricular_detail, name='extracurricular_detail'),
]
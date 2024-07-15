from django.urls import path
from . import views
from django.views.generic.base import RedirectView

# URLconf
urlpatterns = [
    
    path('', views.home),
    path('home',views.home),
    path('main-menu',views.main_menu),
    path('adm-login',views.adm_login),
    path('admin-login',views.admin_login),
    path('admin-logout',views.admin_logout),
    path('insert-student-details',views.insert_student_details),
    path('ins-student-details',views.ins_student_details),
    path('insert-fees-record',views.insert_fees_record),
    path('ins-fees-record',views.ins_fees_record),
    path('del/<int:id>', views.dele),
    path('edit/<int:id>', views.edit),
    path('edcode/<int:id>',views.edcode),
    path('edit-admission-date/<int:id>', views.edit_admission_date),
    path('edcode-admission-date/<int:id>',views.edcode_admission_date),
    path('edit-fees-record/<int:id>', views.edit_fees_record),
    path('edcode-fees-record/<int:id>', views.edcode_fees_record),
    path('feesrecord', views.feesrecord),
    path('credits', views.credits),    
]
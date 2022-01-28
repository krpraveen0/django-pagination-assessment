from django.contrib import admin

from employees.models import Employee, CustomPaginate


admin.site.register(Employee)
admin.site.register(CustomPaginate)

from django.contrib import admin
from .models import Name,EmpID,Address,Contact

# Register your models here.
admin.site.register(Name)
admin.site.register(EmpID)
admin.site.register(Address)
admin.site.register(Contact)

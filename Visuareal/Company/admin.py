from django.contrib import admin
from Company.models import AddCustomer, CompanyInventory, AddCompany


class AddCustomerInline(admin.StackedInline):
	model = AddCustomer
	extra = 0 

class CompanyInventoryInline(admin.StackedInline):
	model = CompanyInventory
	extra = 0

class AddCompanyAdmin(admin.ModelAdmin):
	inlines = [AddCustomerInline, CompanyInventoryInline]
	model = AddCompany

admin.site.register(AddCustomer)
admin.site.register(CompanyInventory)
admin.site.register(AddCompany, AddCompanyAdmin)
# Register your models here.

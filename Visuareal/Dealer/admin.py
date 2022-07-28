from django.contrib import admin
from Dealer.models import DealerInventory, AddDealer
# Register your models here.

# class AddCustomerInline(admin.StackedInline):
# 	from Company.models import AddCustomer
# 	model = AddCustomer
# 	extra = 0

class DealerInventoryInline(admin.StackedInline):
	model = DealerInventory
	extra = 0 

class AddDealerAdmin(admin.ModelAdmin):
	from Company.admin import AddCustomerInline
	inlines = [DealerInventoryInline, AddCustomerInline]
	model = AddDealer

admin.site.register(DealerInventory)
admin.site.register(AddDealer, AddDealerAdmin)


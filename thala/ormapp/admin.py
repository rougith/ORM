

from django.contrib import admin
from .models import Loan

# Customize how Loan model appears in Admin
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'name', 'amount', 'interest_rate', 'duration')
    search_fields = ('name', 'customer_id')
    list_filter = ('interest_rate', 'duration')
    ordering = ('customer_id',)

# Register the model with custom admin options
admin.site.register(Loan, LoanAdmin)

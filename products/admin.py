from django.contrib import admin
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from products.models.product_details import ProductDetails
import csv


@admin.action(description='Export as CSV')
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


# Register your models here.
class ProductDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity']
    search_fields = ('id', 'name')
    actions = [export_as_csv]
    list_per_page = 20


admin.site.register(ProductDetails, ProductDetailsAdmin)
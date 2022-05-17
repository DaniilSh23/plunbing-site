from django.contrib import admin
from santech.models import ApplicationsTypes, Masters, ImageForMasters, PriceList, OurWorks, PhotoForWorks


class ApplicationsTypesAdmin(admin.ModelAdmin):
    list_display = ['id', 'applications_type']
    list_display_links = ['id', 'applications_type']


class MastersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'work_experience']
    list_display_links = ['id', 'name', 'age', 'work_experience']


class ImageForMastersAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'for_master']
    list_display_links = ['id', 'image', 'for_master']


class PriceListAdmin(admin.ModelAdmin):
    list_display = ['id', 'works_title', 'works_price']
    list_display_links = ['id', 'works_title', 'works_price']


class PhotoForWorksAdminInlines(admin.StackedInline):
    model = PhotoForWorks


class OurWorksAdmin(admin.ModelAdmin):
    list_display = ['id', 'works_title', 'works_price']
    list_display_links = ['id', 'works_title', 'works_price']
    inlines = [PhotoForWorksAdminInlines]


admin.site.register(ApplicationsTypes, ApplicationsTypesAdmin)
admin.site.register(Masters, MastersAdmin)
admin.site.register(ImageForMasters, ImageForMastersAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(OurWorks, OurWorksAdmin)
# admin.site.register(PhotoForWorks, PhotoForWorksAdminInlines)

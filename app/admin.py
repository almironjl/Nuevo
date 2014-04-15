from django.contrib import admin
from app.models import TypePoint, Contract, UserHasCompany, User, Type, Point, Order, OrderDetail, Scheduler


#class ProductAdmin(admin.ModelAdmin):
#    list_display = ('name',)


class LocalInline(admin.TabularInline):
    model = User
    exclude = ('id',)
    #readonly_fields = ['detalle',]
    extra = 1

#class RestaurantAdmin(admin.ModelAdmin):
#    list_display = ('name',)
#    #inlines = [LocalInline]
#    # exclude = ('id','created_by','deleted', 'codigo_postal_id',)
#    def save_model(self, request, obj, form, change):
#        obj.created_by = request.user.id
#        obj.save()

#    def save_formset(self, request, form, formset, change):
#       if formset.model == Restaurant:
#            instances = formset.save(commit=False)
#            for instance in instances:
#                instance.created_by = request.user.id
#                instance.save()
#        else:
#            formset.save()

class RestaurantBranchAdmin(admin.ModelAdmin):
    list_display = ('restaurant','distrito','name','address','email',)
    # exclude = ('id',)
    list_filter = ('restaurant',)
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='1')
# make_published.short_description = "Mark selected stories as published"

class RestaurantWebsiteAdmin(admin.ModelAdmin):
    list_display = ('created','email', 'nombre', 'website','status_link')
    readonly_fields = ('id','confirmation_token')
    list_filter = ('status',)


admin.site.register(TypePoint)
admin.site.register(Type)
admin.site.register(Point)
admin.site.register(UserHasCompany)
admin.site.register(Contract)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Scheduler)


#admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Restaurant)
#admin.site.register(RestaurantBranch, RestaurantBranchAdmin)
#admin.site.register(Product, ProductAdmin)
#admin.site.register(Category)
#admin.site.register(LocalHasProduct)
#admin.site.register(WorkerCategory)
#admin.site.register(RestaurantWebsite, RestaurantWebsiteAdmin)

from django.contrib import admin

# Register your models here.

from . models import admin_reg_form,contact_reg,user_add_database,category_add_database,unit_add_database,tax_add_database,product_add_database,quo_add_database,purchase_add_database,stock_add_database
admin.site.register(admin_reg_form)
admin.site.register(contact_reg)
admin.site.register(user_add_database)
admin.site.register(category_add_database)
admin.site.register(unit_add_database)
admin.site.register(tax_add_database)
admin.site.register(product_add_database)
admin.site.register(quo_add_database)
admin.site.register(purchase_add_database)
admin.site.register(stock_add_database)













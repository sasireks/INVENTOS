from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('feature',views.feature,name='feature'),   
    path('service',views.service,name='service'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('admin_index',views.admin_index,name='admin_index'),

    
    path('user view',views.userview,name='user view'),
    path('user management add',views.usermanagementadd,name='user management add'),
    path('usermanagementadd_form_sub',views.usermanagementadd_form_sub,name='usermanagementadd_form_sub'),
    path('edit user add/<int:id>',views.edituseradd,name='edit user add'),
    path('edituseradd_update_form_sub/<int:id>',views.edituseradd_update_form_sub,name='edituseradd_update_form_sub'),
    path('edituseradd_delete/<int:id>',views.edituseradd_delete,name='edituseradd_delete'),

    path('category_list',views.category_list,name='category_list'),
    path('category add',views.categoryadd,name='category add'),
    path('categoryadd_form_sub',views.categoryadd_form_sub,name='categoryadd_form_sub'),
    path('edit_category add/<int:id>',views.edit_categoryadd,name='edit_category add'),
    path('edit_categoryadd_update_form_sub/<int:id>',views.edit_categoryadd_update_form_sub,name='edit_categoryadd_update_form_sub'),
    path('edit_categoryadd_delete/<int:id>',views.edit_categoryadd_delete,name='edit_categoryadd_delete'),


    path('unit list',views.unitlist,name='unit list'),
    path('unit add',views.unitadd,name='unit add'),
    path('unitlist_form_sub',views.unitlist_form_sub,name='unitlist_form_sub'),
    path('edit unit add/<int:id>',views.editunitadd,name='edit unit add'),
    path('editunitadd_update_form_sub/<int:id>',views.editunitadd_update_form_sub,name='editunitadd_update_form_sub'),
    path('editunitadd_delete/<int:id>',views.editunitadd_delete,name='editunitadd_delete'),


    path('taxlist',views.taxlist,name='taxlist'),
    path('tax add',views.taxadd,name='tax add'),
    path('taxadd_form_sub',views.taxadd_form_sub,name='tax_add_database'),
    path('edit tax add/<int:id>',views.edittaxadd,name='edit tax add'),
    path('edittaxadd_update_form_sub/<int:id>',views.edittaxadd_update_form_sub,name='edittaxadd_update_form_sub'),
    path('edittaxadd_delete/<int:id>',views.edittaxadd_delete,name='edittaxadd_delete'),




    path('product list',views.productlist,name='product list'),
    path('product add',views.productadd,name='product add'),
    path('productadd_form_sub',views.productadd_form_sub,name='productadd_form_sub'),
    path('edit product add/<int:id>',views.editproductadd,name='edit product add'),
    path('editproductadd_update_form_sub/<int:id>',views.editproductadd_update_form_sub,name='editproductadd_update_form_sub'),
    path('editproductadd_delete/<int:id>',views.editproductadd_delete,name='editproductadd_delete'),



    path('quo add',views.quoadd,name='quo add'),
    path('quoadd_form_sub',views.quoadd_form_sub,name='quoadd_form_sub'),
    path('edit quo add/<int:id>',views.editquoadd,name='edit quo add'),
    path('editquoadd_update_form_sub/<int:id>',views.editquoadd_update_form_sub,name='editquoadd_update_form_sub'),
    path('editquoadd_delete/<int:id>',views.editquoadd_delete,name='editquoadd_delete'),








    path('contact',views.contact,name='contact'),
    path('Error 404',views.Error404,name='Error 404'),
    path('quo list',views.quolist,name='quo list'),



    path('purchase list',views.purchaselist,name='purchase list'),
    path('purchase add',views.purchaseadd,name='purchase add'),
    path('purchaseadd_form_sub',views.purchaseadd_form_sub,name='purchaseadd_form_sub'),
    path('edit purchase add/<int:id>',views.editpurchaseadd,name='edit purchase add'),
    path('editpurchaseadd_update_form_sub/<int:id>',views.editpurchaseadd_update_form_sub,name='editpurchaseadd_update_form_sub'),
    path('editpurchaseadd_delete/<int:id>',views.editpurchaseadd_delete,name='editpurchaseadd_delete'),






    
    path('stock add',views.stockadd,name='stock add'),
    path('stockadd_form_sub',views.stockadd_form_sub,name='stockadd_form_sub'),
    path('edit stock add/<int:id>',views.editstockadd,name='edit stock add'),
    path('editstockadd_update_form_sub/<int:id>',views.editstockadd_update_form_sub,name='editstockadd_update_form_sub'),
    path('editstockadd_delete/<int:id>',views.editstockadd_delete,name='editstockadd_delete'),



    path('stock list',views.stocklist,name='stock list'),
    path('sales list',views.saleslist,name='sales list'),
    path('Return Product',views.ReturnProduct,name='Return Product'),
    path('admin login new',views.adminloginnew,name='admin login new'),
    path('admin_reg',views.admin_reg,name='admin_reg'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('contact_reg_sub',views.contact_reg_sub,name='contact_reg_sub'),
    
    
    


]     

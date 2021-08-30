from django.shortcuts import render,redirect
from . models import admin_reg_form,contact_reg,user_add_database,category_add_database,unit_add_database,tax_add_database,product_add_database,quo_add_database,purchase_add_database,stock_add_database
from django.contrib import messages

#multiple user_login concept
inventos_user_name=''








# Create your views here.
def index(request):
    return render(request,'index.html')

def feature(request):
    return render(request,'feature.html')   
def service(request):
    return render(request,'service.html')   
def portfolio(request):
    return render(request,'portfolio.html')    
def admin_index(request):
    return render(request,'admin_index.html')    
def userview(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)  
    view_data=user_add_database.objects.all() 
    return render(request,'user view.html',{'inventos_data':inventos_data,'view_data':view_data})  
def usermanagementadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    return render(request,'user management add.html',{'inventos_data':inventos_data})
def usermanagementadd_form_sub(request):   
    if request.method=='POST':
        ex1=user_add_database(email_id=request.POST['email_id'],
                              password=request.POST['password'],
                              user_management_add_file=request.POST['user_management_add_file'],
                              confirmpassword=request.POST['confirm password'],
                              selectstate1=request.POST['selectstate1'],
                              selectstate2=request.POST['selectstate2'])
        ex1.save() 
        messages.error(request,'your data has been successfully saved...!',extra_tags="reg")    
        return redirect(userview)                  
        
        

    return render(request,'user management add.html') 
def edituseradd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=user_add_database.objects.get(id=id)
    return render(request,'edit user add.html',{'inventos_data':inventos_data,'view_data':view_data}) 

def edituseradd_update_form_sub(request,id):
    if request.method=='POST':
        if user_add_database.objects.filter(id=id).exists():
            ex1=user_add_database.objects.filter(id=id).update(email_id=request.POST['email_id'],
                                                               password=request.POST['password'],
                                                               user_management_add_file=request.POST['user_management_add_file'],
                                                               confirmpassword=request.POST['confirmpassword'],
                                                               selectstate1=request.POST['selectstate1'],
                                                               selectstate2=request.POST['selectstate2'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(userview) 
        else:
            return render(request,'edit user add.html')  
def edituseradd_delete(request,id):
    ex1=user_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been successfully deleted.....!',extra_tags='danger')
    return redirect(userview)
    return render(request,'edit user add.html')                                                             
    







def category_list(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_date=category_add_database.objects.all()
    return render(request,'category_list.html',{'inventos_data':inventos_data,'view_date':view_date}) 
def categoryadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    return render(request,'category add.html',{'inventos_data':inventos_data})
def edit_categoryadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    views_datas=category_add_database.objects.get(id=id)
    
    return render(request,'edit_category add.html',{'inventos_data':inventos_data,'views_datas':views_datas})
def edit_categoryadd_update_form_sub(request,id): 
    if request.method=='POST':
        if category_add_database.objects.filter(id=id).exists():
            ex1=category_add_database.objects.filter(id=id).update(name=request.POST['name'],
                                                                category_add_file=request.POST['category_add_file'],
                                                                parent_category=request.POST['parent_category'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(category_list) 
        else:
            return render(request,'edit_category add.html')
def edit_categoryadd_delete(request,id):
    ex1=category_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been successfully deleted.....!',extra_tags='danger')
    return redirect(category_list)
               

                                                                
    return render(request,'edit_category add.html')

def categoryadd_form_sub(request):
    if request.method=='POST':
        ex1=category_add_database(name=request.POST['name'],
                                  category_add_file=request.POST['category_add_file'],
                                  parent_category=request.POST['parent_category'])
        ex1.save() 
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(category_list)   

    else:
        return render(request,'edit_category add.html')    
    
    
    






def unitlist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=unit_add_database.objects.all()
    return render(request,'unit list.html',{'inventos_data':inventos_data,'view_data':view_data})  
def unitlist_form_sub(request):
    if request.method=='POST':
        ex1=unit_add_database(code=request.POST['code'],
                              name=request.POST['name'])
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(unitlist)                       
    return render(request,'unit list.html')
def editunitadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=unit_add_database.objects.get(id=id)
    return render(request,'edit unit add.html',{'inventos_data':inventos_data,'view_data':view_data}) 
def editunitadd_update_form_sub(request,id):
    if request.method=='POST':
        if unit_add_database.objects.filter(id=id).exists():
            ex1=unit_add_database.objects.filter(id=id).update(code=request.POST['code'],
                                                               name=request.POST['name'])
            
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(unitlist) 
        else:
            return render(request,'edit unit add.html')    
        
    return render(request,'edit unit add.html')  
def editunitadd_delete(request,id):
    ex1=unit_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been successfully deleted.....!',extra_tags='danger')
    return redirect(unitlist)
               

    return render(request,'unit list.html')     
                                                       
            

      




def unitadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    return render(request,'unit add.html',{'inventos_data':inventos_data})  



def taxlist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=tax_add_database.objects.all()
    return render(request,'taxlist.html',{'inventos_data':inventos_data,'view_data':view_data}) 
def taxadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    return render(request,'tax add.html',{'inventos_data':inventos_data}) 
def taxadd_form_sub(request):
    if request.method=='POST':
        ex1=tax_add_database(tax_name=request.POST['tax_name'],
                             rate=request.POST['rate'])
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(taxlist)                    
    return render(request,'tax add.html')  
def edittaxadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=tax_add_database.objects.get(id=id)
    return render(request,'edit tax add.html',{'inventos_data':inventos_data,'view_data':view_data})    


def edittaxadd_update_form_sub(request,id):
    if request.method=='POST':
        if tax_add_database.objects.filter(id=id).exists():
            ex1=tax_add_database.objects.filter(id=id).update(tax_name=request.POST['tax_name'],
                                                              rate=request.POST['rate'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(taxlist) 
        else:
            return render(request,'edit tax add.html')   
    return render(request,'edit tax add.html')

def edittaxadd_delete(request,id):
    ex1=tax_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been successfully deleted.....!',extra_tags='danger')
    return redirect(taxlist)
               
     











def productlist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=product_add_database.objects.all()
    return render(request,'product list.html',{'inventos_data':inventos_data,'view_data':view_data}) 
def productadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)  
    return render(request,'product add.html',{'inventos_data':inventos_data})  
def productadd_form_sub(request):
    if request.method=='POST':
        ex1=product_add_database(select_Category=request.POST['select_Category'],
                                 select_brand=request.POST['select_brand'],
                                 select_unit=request.POST['select_unit'],
                                 enter_barcode=request.POST['enter_barcode'],
                                 product_cost=request.POST['product_cost'],
                                 product_sales_price=request.POST['product_sales_price'],
                                 product_alert_quantatity=request.POST['product_alert_quantatity'],
                                 product_image=request.POST['product_image'],
                                 tax_type=request.POST['tax_type'],
                                 product_name=request.POST['product_name'])
                                 
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(productlist)                    
    return render(request,'product add.html')  


def editproductadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=product_add_database.objects.get(id=id) 
    return render(request,'edit product add.html',{'inventos_data':inventos_data,'view_data':view_data}) 

def editproductadd_update_form_sub(request,id):
    if request.method=='POST':
        if product_add_database.objects.filter(id=id).exists():
            ex1=product_add_database.objects.filter(id=id).update(select_Category=request.POST['select_Category'],
                                                                  select_brand=request.POST['select_brand'],
                                                                  select_unit=request.POST['select_unit'],
                                                                  enter_barcode=request.POST['enter_barcode'],
                                                                  product_cost=request.POST['product_cost'],
                                                                  product_sales_price=request.POST['product_sales_price'],
                                                                  product_alert_quantatity=request.POST['product_alert_quantatity'],
                                                                  product_image=request.POST['product_image'],
                                                                  tax_type=request.POST['tax_type'],
                                                                  product_name=request.POST['product_name'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(productlist) 
        else:
            return render(request,'edit product add.html')   
                                                         
def editproductadd_delete(request,id):
    ex1=product_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully.........!!!',extra_tags='danger')
    return redirect(productlist) 
                                                           


                    


def quoadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)  
    return render(request,'quo add.html',{'inventos_data':inventos_data}) 
def quoadd_form_sub(request):
    if request.method=='POST':
        ex1=quo_add_database(from_warehouse=request.POST['from_warehouse'],
                             to_warhouse=request.POST['to_warhouse'],
                             shippping_cost=request.POST['shippping_cost'],
                             select_state=request.POST['select_state'],
                             product_name=request.POST['product_name'],
                             quantatity=request.POST['quantatity'],
                             unit_price=request.POST['unit_price'],
                             product_image=request.POST['product_image'])
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(quolist)                    
                       
    return render(request,'quo add.html')
def editquoadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=quo_add_database.objects.get(id=id)
    return render(request,'edit quo add.html',{'inventos_data':inventos_data,'view_data':view_data})
def editquoadd_update_form_sub(request,id):
    if request.method=='POST':
        if quo_add_database.objects.filter(id=id).exists():
            ex1=quo_add_database.objects.filter(id=id).update(from_warehouse=request.POST['from_warehouse'],
                                                          to_warhouse=request.POST['to_warhouse'],
                                                          shippping_cost=request.POST['shippping_cost'],
                                                          select_state=request.POST['select_state'],
                                                          product_name=request.POST['product_name'],
                                                          quantatity=request.POST['quantatity'],
                                                          unit_price=request.POST['unit_price'],
                                                          product_image=request.POST['product_image'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(quolist) 
        else:
            return render(request,'edit quo add.html')   
def editquoadd_delete(request,id):
    ex1=quo_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully.........!!!',extra_tags='danger')
    return redirect(quolist) 
                                                                 
    


























def contact(request):
    return render(request,'contact.html') 
def Error404(request):
    return render(request,'Error 404.html')  
def quolist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=quo_add_database.objects.all()
    return render(request,'quo list.html',{'inventos_data':inventos_data,'view_data':view_data}) 





def purchaselist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=purchase_add_database.objects.all() 
    return render(request,'purchase list.html',{'inventos_data':inventos_data,'view_data':view_data})     
def purchaseadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)   
    return render(request,'purchase add .html',{'inventos_data':inventos_data}) 
def purchaseadd_form_sub(request):
    if request.method=='POST':
        ex1=purchase_add_database(select_warehouse=request.POST['select_warehouse'],
                                 select_supplier=request.POST['select_supplier'],
                                 select_state=request.POST['select_state'],
                                 product_name=request.POST['product_name'],
                                 quantatity=request.POST['quantatity'],
                                 unit_price=request.POST['unit_price'],
                                 product_image=request.POST['product_image'])
         
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(purchaselist)                          
    return render(request,'purchase add .html')
def editpurchaseadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name) 
    view_data=purchase_add_database.objects.get(id=id)
    return render(request,'edit purchase add.html',{'inventos_data':inventos_data,'view_data':view_data})

def editpurchaseadd_update_form_sub(request,id):
    if request.method=='POST':
        if purchase_add_database.objects.filter(id=id).exists():
            ex1=purchase_add_database.objects.filter(id=id).update(select_warehouse=request.POST['select_warehouse'],
                                                                   select_supplier=request.POST['select_supplier'],
                                                                   select_state=request.POST['select_state'],
                                                                   product_name=request.POST['product_name'],
                                                                   quantatity=request.POST['quantatity'],
                                                                   unit_price=request.POST['unit_price'],
                                                                   product_image=request.POST['product_image'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(purchaselist) 
        else:
            return render(request,'edit purchase add.html')     


def editpurchaseadd_delete(request,id):
    ex1=purchase_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully.........!!!',extra_tags='danger')
    return redirect(purchaselist) 
    


    


































def stockadd(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)   
    return render(request,'stock add.html',{'inventos_data':inventos_data}) 
def stockadd_form_sub(request):
    if request.method=='POST':
        ex1=stock_add_database(from_warehouse=request.POST['from_warehouse'],
                               to_warehouse=request.POST['to_warehouse'],
                               shipping_cost=request.POST['shipping_cost'],
                               select_state=request.POST['select_state'],
                               product_name=request.POST['product_name'],
                               quantatity=request.POST['quantatity'],
                               unit_price=request.POST['unit_price'],
                               product_image=request.POST['product_image'],)
         
        ex1.save()  
        messages.error(request,'your data has been saved successfully.....!',extra_tags="reg")  
        return redirect(stocklist)                      
                               
    return render(request,'stock add.html')

        

def editstockadd(request,id):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=stock_add_database.objects.get(id=id)
    return render(request,'edit stock add.html',{'inventos_data':inventos_data,'view_data':view_data})


def editstockadd_update_form_sub(request,id):
    if request.method=='POST':
        if stock_add_database.objects.filter(id=id).exists():
            ex1=stock_add_database.objects.filter(id=id).update(from_warehouse=request.POST['from_warehouse'],
                                                                to_warehouse=request.POST['to_warehouse'],
                                                                shipping_cost=request.POST['shipping_cost'],
                                                                select_state=request.POST['select_state'],
                                                                product_name=request.POST['product_name'],
                                                                quantatity=request.POST['quantatity'],
                                                                unit_price=request.POST['unit_price'],
                                                                product_image=request.POST['product_image'])
            messages.error(request,'your data has been successfully updated.....!',extra_tags='reg')  
            return redirect(stocklist) 
        else:
            return render(request,'edit stock add.html')            


def editstockadd_delete(request,id):
    ex1=stock_add_database.objects.get(id=id)
    ex1.delete()
    messages.error(request,'your data has been deleted successfully.........!!!',extra_tags='danger')
    return redirect(stocklist) 
    
    
















def stocklist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)
    view_data=stock_add_database.objects.all()  
    return render(request,'stock list.html',{'inventos_data':inventos_data,'view_data':view_data})  






def saleslist(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)   
    return render(request,'sales list.html',{'inventos_data':inventos_data})      
def ReturnProduct(request):
    inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)  
    return render(request,'Return Product.html',{'inventos_data':inventos_data})  
def adminloginnew(request):
    return render(request,'admin login new.html')      
def admin_reg(request):
    if request.method=='POST':
        if admin_reg_form.objects.filter(user_name=request.POST['user_name']).exists():
            messages.error(request,'This Username Has Already Taken!!.....',extra_tags='login')
        elif admin_reg_form.objects.filter(email_id=request.POST['email_id']):
            messages.error(request,'This Email Id Has Already Taken!!....',extra_tags='login')    

        else:






         ex1=admin_reg_form(user_name=request.POST['user_name'],
                           password=request.POST['password'],
                           repeat_password=request.POST['repeat_password'],
                           email_id=request.POST['email_id']) 
         ex1.save()     
         messages.error(request,'your data has been saved successfully',extra_tags="reg")       
         return render(request,'admin login new.html')                        
                        
        
    return render(request,'admin login new.html')     
def admin_login(request):

    if request.method=='POST':
        if admin_reg_form.objects.filter(user_name=request.POST['user_name'],password=request.POST['password'],).exists():
           ex1=admin_reg_form.objects.get(user_name=request.POST['user_name'],password=request.POST['password'],)
           global inventos_user_name 
           inventos_user_name=ex1.user_name
           print("check:",inventos_user_name)
           inventos_data=admin_reg_form.objects.get(user_name=inventos_user_name)

           return render(request,'admin_index.html',{'inventos_data':inventos_data})












             
        else:
            messages.error(request,'your username or password is incorrect',extra_tags="login")
            return render(request,'admin login new.html')


    return render(request,'admin login new.html')   


def contact_reg_sub(request):
    if request.method=='POST':
        ex1=contact_reg(user_name=request.POST['user_name'],
                        email_id=request.POST['email_id'],
                        subject=request.POST['subject'],
                        comment=request.POST['comment'])
        ex1.save()  
        messages.error(request,'your contact details has been saved successfully......!',extra_tags='contact')              
                

    return render(request,'contact.html')   





    




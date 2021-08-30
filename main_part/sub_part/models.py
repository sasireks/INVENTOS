from django.db import models

# Create your models here.

class admin_reg_form(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    repeat_password=models.CharField(max_length=100)
    email_id=models.EmailField()

    def __str__(self):
        return self.user_name

class contact_reg(models.Model):
    user_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    subject=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)   

    def __str__(self):
        return self.user_name  

class user_add_database(models.Model):
    email_id=models.EmailField()
    password=models.CharField(max_length=100)
    user_management_add_file=models.FileField(upload_to="documents")
    confirmpassword=models.CharField(max_length=100)
    selectstate1=models.CharField(max_length=100)
    selectstate2=models.CharField(max_length=100)

    def __str__(self):
        return self.email_id

   
class category_add_database(models.Model):
    name=models.CharField(max_length=100)  
    category_add_file=models.FileField(upload_to="documents")     
    parent_category=models.CharField(max_length=100) 

    def __str__(self):
        return self.name   

class unit_add_database(models.Model):
    code=models.CharField(max_length=100)   
    name=models.CharField(max_length=100)   

    def __str__(self):
        return self.name  


class tax_add_database(models.Model):
    tax_name=models.CharField(max_length=100)  
    rate=models.CharField(max_length=100) 

    def __str__(self):
        return self.tax_name   

class product_add_database(models.Model):
    select_Category=models.CharField(max_length=100)
    select_brand=models.CharField(max_length=100)
    select_unit=models.CharField(max_length=100)
    enter_barcode=models.CharField(max_length=100)
    product_cost=models.CharField(max_length=100)
    product_sales_price=models.CharField(max_length=100)
    product_alert_quantatity=models.CharField(max_length=100)
    product_image=models.CharField(max_length=100)
    tax_type=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    


    def __str__(self):
        return self.product_name

             
class quo_add_database(models.Model):
    from_warehouse=models.CharField(max_length=100) 
    to_warhouse=models.CharField(max_length=100) 
    shippping_cost=models.CharField(max_length=100)  
    select_state=models.CharField(max_length=100) 
    product_name=models.CharField(max_length=100)
    quantatity=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    product_image=models.CharField(max_length=100)

    def __str__(self):
        return self.select_state

class purchase_add_database(models.Model):
    select_warehouse=models.CharField(max_length=100)
    select_supplier=models.CharField(max_length=100)
    select_state=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    quantatity=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    product_image=models.CharField(max_length=100) 


    def __str__(self):
        return self.product_name       

class stock_add_database(models.Model):
    from_warehouse=models.CharField(max_length=100)
    to_warehouse=models.CharField(max_length=100)
    shipping_cost=models.CharField(max_length=100)
    select_state=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    quantatity=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    product_image=models.CharField(max_length=100)

    def __str__(self):
        return self.product_name














             
             
             


  




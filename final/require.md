make dir static for static file https://wachira.ece.engr.tu.ac.th/cn334/682/static-files.zip

https://wachira.ece.engr.tu.ac.th/cn334/682/product_product.csv import SQLite

base.html for parent templete
create_product.html , read_product.html, update_product.html delete_product.html for child templete

django app name product and make model 
name for product name charfield, max_length=150
price for price per unit decimalField max_digit=10 decimal_places =2
quantity for unit in stock integerfield
category charfield max_length=100

Use ModelForm

for visulixation
localhost:8000/product/read

in base
logo on top of table
6610625037 Arefandy Waeouseng under logo

table name : Product Details
text Maximum total: display product name and ยอดรวมมูลค่าสูงสุด
ฺbutton : Add A New Product to add new page
table
colum # แสดงลำดับ
colum Name Price Quantity Category แสดงตามลำดับ
colum total : price * quantity แสดงทศนิยม 2 ตำแหน่ง
colum Action : แสดง icon สำหรับแก้ข้อมูล

/product/create

logo on top of table
6610625037 Arefandy Waeouseng under logo
change Product Details to Create Product

NAME : text field
PRICE : text field
QUANTITY : text field
CATEGORY : Drop down (use in csv for all category that have)
Button : Create
text that can click to go back: Back to Product List 

when user click create

logo on top of table
6610625037 Arefandy Waeouseng under logo
change Product Details to Product Created

text : Name: Product name
text: Price: price, Qty: 3, Category: category
Button : Add A New Product after click redirect back to /read
text that can click to go back: Back to Product List 


product/update/<id>

logo on top of table
6610625037 Arefandy Waeouseng under logo
change Product Details to Update Product

NAME : text field
PRICE : text field
QUANTITY : text field
CATEGORY : Drop down (use in csv for all category that have)
Button : Update after click redirect back to /read
text that can click to go back: Back to Product List 

product/delete/<id>

logo on top of table
6610625037 Arefandy Waeouseng under logo
change Product Details to Delete Product

text : Are you sure you want to delete the product "Product Name"

Button : Confirm Delete after click redirect back to /read
text that can click to go back: Back to Product List 



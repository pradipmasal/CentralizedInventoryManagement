from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home'),
    path('vendor-list', vendor_list, name='vendor-list'),
    path('create-vendor/', vendor_create, name='vendor-create'),
    path('update-vendor/<int:pk>/', vendor_update, name='vendor-update'),
    path('delete-vendor/<int:pk>/', vendor_delete, name='vendor-delete'),
    path('category-list', category_list, name='category-list'),
    path('create-category/', category_create, name='category-create'),
    path('update-category/<int:pk>/', category_update, name='category-update'),
    path('delete-category/<int:pk>/', category_delete, name='category-delete'),
    path('subcategory/', subcategory_list, name='subcategory-list'),
    path('subcategory/create/', subcategory_create, name='subcategory-create'),
    path('subcategory/update/<int:pk>/', subcategory_update, name='subcategory-update'),
    path('subcategory/delete/<int:pk>/', subcategory_delete, name='subcategory-delete'),
    path('unit/', unit_list, name='unit-list'),
    path('unit/create/', unit_create, name='unit-create'),
    path('unit/update/<int:pk>/', unit_update, name='unit-update'),
    path('unit/delete/<int:pk>/', unit_delete, name='unit-delete'),
    path('product/', product_list, name='product-list'),
    path('product/create/', product_create, name='product-create'),
    path('product/update/<int:pk>/', product_update, name='product-update'),
    path('product/delete/<int:pk>/', product_delete, name='product-delete'),
    path('purchase/', purchase_list, name='purchase-list'),
    path('purchase/create/', purchase_create, name='purchase-create'),
    path('purchase/update/<int:pk>/', purchase_update, name='purchase-update'),
    path('purchase/delete/<int:pk>/', purchase_delete, name='purchase-delete'),
    path('customers/', customer_list, name='customer-list'),
    path('customers/create/', customer_create, name='customer-create'),
    path('customers/<int:pk>/edit/', customer_update, name='customer-update'),
    path('customers/<int:pk>/delete/', customer_delete, name='customer-delete'),
    path('warehouses/', warehouse_list, name='warehouse-list'),
    path('warehouses/create/', warehouse_create, name='warehouse-create'),
    path('warehouses/<int:pk>/edit/', warehouse_update, name='warehouse-update'),
    path('warehouses/<int:pk>/delete/', warehouse_delete, name='warehouse-delete'),
    path('purchase-product-sales/', purchase_product_sale_list, name='purchase-product-sale-list'),
    path('purchase-product-sales/create/', purchase_product_sale_create, name='purchase-product-sale-create'),
    path('purchase-product-sales/<int:pk>/update/', purchase_product_sale_update, name='purchase-product-sale-update'),
    path('purchase-product-sales/<int:pk>/delete/', purchase_product_sale_delete, name='purchase-product-sale-delete'),
    path('sales/', sale_list, name='sale-list'),
    path('sales/create/', sale_create, name='sale-create'),
    path('sales/<int:pk>/update/', sale_update, name='sale-update'),
    path('sales/<int:pk>/delete/', sale_delete, name='sale-delete'),
]

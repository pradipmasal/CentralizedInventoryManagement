# test.py
from django.utils import timezone
from management.models import Vendor, Category, SubCategory, Unit, Product, Purchase, PurchaseProduct, PurchaseReturn
from management.models import PurchaseProductSale, CustomerDetails, Warehouse, Sale, SaleProduct, SaleReturn, Inventory, StockTransfer

def create_sample_data():
    # Create Categories and SubCategories
    category1 = Category.objects.create(name="Apparel")
    category2 = Category.objects.create(name="Accessories")

    subcategory1 = SubCategory.objects.create(name="Hoodies", category=category1)
    subcategory2 = SubCategory.objects.create(name="Hats", category=category2)

    # Create Units
    unit1 = Unit.objects.create(name="Piece")
    unit2 = Unit.objects.create(name="Box")

    # Create Vendors
    vendor1 = Vendor.objects.create(name="Vendor One", gst="GST12345", details="Supplier of Apparel")
    vendor2 = Vendor.objects.create(name="Vendor Two", gst="GST67890", details="Supplier of Accessories")

    # Create Products
    product1 = Product.objects.create(name="Basic Hoodie", vendor=vendor1, category=category1, sub_category=subcategory1, 
                                      reorder_level=10, unit=unit1, barcode="1234567890")
    product2 = Product.objects.create(name="Stylish Hat", vendor=vendor2, category=category2, sub_category=subcategory2, 
                                      reorder_level=5, unit=unit2, barcode="9876543210")

    # Create Purchase Orders
    purchase1 = Purchase.objects.create(purchase_date=timezone.now(), vendor_invoice_number="INV001", vendor=vendor1, total=5000.00)
    purchase2 = Purchase.objects.create(purchase_date=timezone.now(), vendor_invoice_number="INV002", vendor=vendor2, total=1500.00)

    # Create Purchase Products
    purchase_product1 = PurchaseProduct.objects.create(purchase=purchase1,product=product1, quantity=10, price=450, gst_percent=18, total=5400)
    purchase_product2 = PurchaseProduct.objects.create(purchase=purchase2,product=product2, quantity=5, price=300, gst_percent=18, total=1800)

    # Create Purchase Product Sale
    purchase_product_sale1 = PurchaseProductSale.objects.create(purchase_product=purchase_product1, margin_percent=15, 
                                                                total_margin=810, discount=10, selling_price=500, selling_gst=18)
    purchase_product_sale2 = PurchaseProductSale.objects.create(purchase_product=purchase_product2, margin_percent=20, 
                                                                total_margin=360, discount=5, selling_price=350, selling_gst=18)

    # Create Customers
    customer1 = CustomerDetails.objects.create(name="John Doe", gst_number="GST101", mobile="9999999999", details="VIP customer")
    customer2 = CustomerDetails.objects.create(name="Jane Smith", gst_number="GST102", mobile="8888888888", details="Regular customer")

    # Create Warehouses
    warehouse1 = Warehouse.objects.create(name="Warehouse One", mobile="1234567890", gst_number="GST111", details="Main Warehouse")
    warehouse2 = Warehouse.objects.create(name="Warehouse Two", mobile="0987654321", gst_number="GST112", details="Secondary Warehouse")

    # Create Sales
    sale1 = Sale.objects.create(warehouse=warehouse1, customer=customer1, gst=18, subtotal=5000, total=5900)
    sale2 = Sale.objects.create(warehouse=warehouse2, customer=customer2, gst=18, subtotal=1500, total=1770)

    # Create Sale Products
    sale_product1 = SaleProduct.objects.create(sale=sale1,purchase_product_sale=purchase_product_sale1, quantity=5, total=2500)
    sale_product2 = SaleProduct.objects.create(sale=sale2,purchase_product_sale=purchase_product_sale2, quantity=3, total=1050)

    # Create Sale Returns
    sale_return1 = SaleReturn.objects.create(sale=sale1, product=product1, quantity=2, reason="Damaged", return_date=timezone.now())
    sale_return2 = SaleReturn.objects.create(sale=sale2, product=product2, quantity=1, reason="Customer Request", return_date=timezone.now())

    # Create Inventory
    inventory1 = Inventory.objects.create(product=product1, quantity_available=100, reorder_level=20, warehouse=warehouse1, last_updated=timezone.now())
    inventory2 = Inventory.objects.create(product=product2, quantity_available=50, reorder_level=10, warehouse=warehouse2, last_updated=timezone.now())

    # Create Stock Transfers
    stock_transfer1 = StockTransfer.objects.create(source_warehouse=warehouse1, destination_warehouse=warehouse2, 
                                                   product=product1, quantity=20, transfer_date=timezone.now(), remarks="Restock")
    stock_transfer2 = StockTransfer.objects.create(source_warehouse=warehouse2, destination_warehouse=warehouse1, 
                                                   product=product2, quantity=10, transfer_date=timezone.now(), remarks="Restock")

    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data()
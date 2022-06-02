from django.shortcuts import render
from .models import Product, Product_Purchase, Vendor, Vendor_Sale


# Create your views here.

def index(request):
    products_name = []
    Purchase_price = []
    Sell_price = []
    Profit = []
    vendorsales = Vendor_Sale.objects.all()
    product_Purchases = Product_Purchase.objects.all()
    for vendorsale in vendorsales:
        for product_Purchase in product_Purchases:
            if product_Purchase.product == vendorsale.product:
                products_name.append(vendorsale.product)
                Sell_price.append(vendorsale.price)
                Purchase_price.append(product_Purchase.price)
                Profit.append(vendorsale.price-product_Purchase.price)
    my_list = Sell_price
    total_Sell_price = sum(my_list)

    my_list2 = Purchase_price
    total_Purchase_price = sum(my_list2)

    my_list3 = Profit
    total_Profit = sum(my_list3)


    context = {'products_name':products_name,
               'Sell_price':Sell_price,
               'Purchase_price':Purchase_price,
               'Profit':Profit,
               'total_Sell_price':total_Sell_price,
               'total_Purchase_price':total_Purchase_price,
               'total_Profit':total_Profit}
    return render(request, 'index.html',context)

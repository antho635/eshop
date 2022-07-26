from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from store.models import Product, Cart, Order, Category


def style(request):
    return render(request, "shop/style.css")


# index
def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, "store/category.html", context={"products": products, "category": category})


# product_detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'product': product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request, "store/cart.html", context={"orders": cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect("index")

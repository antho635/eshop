import cart as cart
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from store.views import index, product_detail, add_to_cart, cart, style
from accounts.views import login_user, logout_user, signup

from shop import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # style
                  path('style.css', style, name='style'),
                  path('', index, name='index'),
                  path('signup/', signup, name='signup'),
                  path('login/', login_user, name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('product/<str:slug>/', product_detail, name='product'),
                  path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
                  path('cart/', cart, name='cart'),
                  # path('cart/delete/', delete_cart, name='delete-cart'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

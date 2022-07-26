from django.conf.urls.static import static

from accounts import views
from accounts.views import signup, logout_user, login_user, my_account
from shop import settings
from store.views import index, product_detail, add_to_cart, cart, delete_cart, style
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # style
                  path('style.css', style, name='style'),
                  path('', index, name='index'),
                  path('signup/', signup, name='signup'),
                  path('login/', login_user, name='login'),
                  path('logout/', logout_user, name='logout'),
                  path('cart/', cart, name='cart'),
                  path('cart/delete/', delete_cart, name='delete-cart'),
                  path('product/<str:slug>/', product_detail, name='product'),
                  path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
                  # my_account
                 # path('my-account/', my_account, name='my-account'),
                  # accounts
                 # path('accounts/', include('accounts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

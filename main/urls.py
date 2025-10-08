from django.urls import path
from main.views import show_main, create_product, show_product_detail, show_xml, products_json, show_xml_by_id, show_json_by_id
from main.views import register_ajax, login_ajax, logout_ajax, edit_product, delete_product, create_product_ajax, delete_product_ajax, edit_product_ajax
from main.views import login_user, register, logout_user

app_name = 'main'

# url
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name = 'create_product'),
    path('product/<str:id>/', show_product_detail, name='show_product_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('ajax/login/', login_ajax, name='login_ajax'),
    path('ajax/register/', register_ajax, name='register_ajax'),
    path('ajax/logout/', logout_ajax, name='logout_ajax'),
    path('edit-product/<str:id>/', edit_product, name='edit_product'),
    path('delete-product/<str:id>/', delete_product, name='delete_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-ajax/', create_product_ajax, name='create_product_ajax'),
    path('product/<uuid:product_id>/edit-ajax/', edit_product_ajax, name='edit_product_ajax'),
    path('product/<uuid:product_id>/delete-ajax/', delete_product_ajax, name='delete_product_ajax'),
    path('products/json/', products_json, name='products_json'),
]
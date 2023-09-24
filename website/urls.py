from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_registration_or_login , name='registration_or_login'),
    # path('product/<str:category>/', views.hot),
    path('about_us/', views.about_us, name='about_us'),
    path('watermelon/', views.watermelon, name='watermelon'),
    path('orange/', views.orange, name='orange'),
    path('apple/', views.apple, name='apple'),
    path('mango/', views.mango, name='mango'),
    path('all_products/<str:category>/', views.all_products, name='all_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('all_products/all_products/', views.all_product, name='all_product'),
    path('comment/', views.submit_comment, name='comment_submit_url'),
    path('success/', views.success, name='success_url'),
    path('home/', views.home, name='home'),

    # Add other URL patterns as needed

]

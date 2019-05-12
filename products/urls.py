from django.conf.urls import url, include
from .views import all_products, product_detail, all_products2


urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^$', all_products2, name='all_products2'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
]
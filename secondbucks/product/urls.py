from . import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^$', views.index, name='index'),

    #/college_name/categories
    url('^(?P<college_id>[0-9]+)/categories/$', views.category_list, name='categories'),

    #/college_name/category_name
    url('^(?P<college_id>[0-9]+)/(?P<category_id>[0-9]+)/$', views.category_wise, name='category_wise'),

    #/college_name/category_name/product_name/
    url('^(?P<college_id>[0-9]+)/(?P<category_id>[0-9]+)/(?P<product_id>[0-9]+)/$', views.product_details, name='product_details'),

    #/college/register/
    url('^college/register/$',views.RegisterCollege.as_view(),name='college-add'),

    #/product/add/                                                           
    url('^product/add/$',views.add_product, name='product-add'),

    #/product/add/sell/                                                            
    url('^product/add/sell/$',views.RegisterSellProduct,name='product-add-sell'),

    #/product/add/share/                                                           
    url('^product/add/share/$',views.RegisterShareProduct,name='product-add-share'),

    #register/user/
    url('^register/user/$',views.UserFormView.as_view(),name='register-user'),

    #register/user_id/userdetails/
    url('^register/userdetails/$',views.RegisterUserDetails,name='register-userdetails'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('login',views.login),
    path('signup',views.signup),
    path('showcakes/<id>',views.showcakes),
    path('viewDetails/<id>',views.cakeDetails),
    path('logout',views.logout),
    path('addtocart',views.addtocart),
    path('showAll',views.showAll),
    path('remove/<id>',views.remove),    
    path('payment',views.payment),
    path('removeItem',views.removeItem),
    path('demo',views.demo),
    path('page',views.pagedemo),
]

from unicodedata import name
from django.contrib import admin
from django.urls import path
from Herbal_Life import views



admin.site.site_header = "Herbal Life Admin"
admin.site.site_title = "Herbal Life Admin Portal"
admin.site.index_title = "Welcome to Herbal LIfe"

urlpatterns = [                                              
    path("",views.index,name="Home"),
    path("about",views.about,name = "about"),
    path("products/<int:myid>", views.productView, name="product"),
    path("Event_Registration",views.Event_reg,name="event_registration"),
    path("EVent",views.eVent,name = "Event"),
  
    path("contact",views.contact,name = "contact"),
    path("payment",views.payment,name = "payment"),
    #path('handlerequest',views.handlerequest,name='handlerequest'),
    path('team',views.team,name = 'Our Team'),
    path('getaway', views.getaway,name = 'getaway'),
    path('offline', views.offline , name = 'offline events'),
    path('online',views.online,name = 'offline events'),
    path('weight_loss',views.weight_loss,name="weight loss"),
    path('weight_gain',views.weight_gain,name="weight gain")
    
]
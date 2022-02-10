from multiprocessing import Event
from django.contrib import admin

from .models import Contact,Payment,Product,Event_Registration,EVent

admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Event_Registration)
admin.site.register(EVent)




# Register your models here.

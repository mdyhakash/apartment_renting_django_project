from django.contrib import admin
from .models import User,Property,Booking,Transaction,Review,SavedProperty

# Register your models here.
admin.site.register([User,Property,Booking,Transaction,Review,SavedProperty])

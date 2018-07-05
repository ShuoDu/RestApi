from django.contrib import admin
from .models import Publisher
from .models import Books
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Books)
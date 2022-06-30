from django.contrib import admin
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.site_header = "Newsbook Admin"
admin.site.site_title = "Newsbook Admin Portal"
admin.site.index_title = "Welcome to Newsbook Admin"
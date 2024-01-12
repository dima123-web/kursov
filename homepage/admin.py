from django.contrib import admin
from .models import News, Aktirovka, Workers, Text, Appeal

admin.site.register(News)
admin.site.register(Workers)
admin.site.register(Aktirovka)
admin.site.register(Text)
admin.site.register(Appeal)

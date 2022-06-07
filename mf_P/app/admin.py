from django.contrib import admin

from app.models import token, ariza_E


class TokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(token, TokenAdmin)


class ArizaAdmin(admin.ModelAdmin):
    pass
admin.site.register(ariza_E, ArizaAdmin)

from django.contrib import admin
from .models import NationalNewsChannel,RegionalNewsChannel,Magazine,SocialChannel,Ebook,RegionalNewsPaper,NationalNewsPaper,Article

admin.site.register(RegionalNewsChannel)
admin.site.register(NationalNewsChannel)
admin.site.register(Magazine)
admin.site.register(SocialChannel)
admin.site.register(Ebook)
admin.site.register(RegionalNewsPaper)
admin.site.register(NationalNewsPaper)
admin.site.register(Article)
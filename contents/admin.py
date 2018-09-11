from django.contrib import admin
from .forms import ArticleForm
from .models import (NationalNewsChannel,RegionalNewsChannel,Magazine,SocialChannel,Ebook,RegionalNewsPaper,NationalNewsPaper,Article,Edition,
NewsPaper,State,PublisherDetail,Main_Edition,Sub_Edition)

admin.site.register(RegionalNewsChannel)
admin.site.register(NationalNewsChannel)
admin.site.register(Magazine)
admin.site.register(SocialChannel)
admin.site.register(Ebook)
admin.site.register(RegionalNewsPaper)
admin.site.register(NationalNewsPaper)

class Article_admin(admin.ModelAdmin):
	form = ArticleForm
admin.site.register(Article)

admin.site.register(NewsPaper)
admin.site.register(Edition)
admin.site.register(State)
admin.site.register(PublisherDetail)
admin.site.register(Main_Edition)
admin.site.register(Sub_Edition)
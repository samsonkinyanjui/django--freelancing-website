from django.contrib import admin
from . models import writer,Bids,pay,comp
# Register your models here.

class reg1(admin.ModelAdmin):
    list_display=('first_name','second_name','username','email','phone','last_login','created','inviter_name','number')
class reg2(admin.ModelAdmin):
    list_display=('post','cat','price','per','code','status')
class reg3(admin.ModelAdmin):
    list_display=('username','code1','mpesa_code')
class reg4(admin.ModelAdmin):
    list_display=('upload1','username','mpesa_code','code')
    


admin.site.register(writer, reg1)
admin.site.register(Bids,reg2)
admin.site.register(pay,reg3)
admin.site.register(comp,reg4)

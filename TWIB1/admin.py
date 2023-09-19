from django.contrib import admin
from .models import *
from django.urls import path
from django.shortcuts import render
from django import forms

# Register your models here.
class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()
class WebpageAdmin(admin.ModelAdmin):
    list_display=('name','type','photo','description')


class ContentAdmin(admin.ModelAdmin):
    list_display=('name','type','pic','des','rate','link')
    search_fields=Content.SearchableFields

    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csv/',self.upload_csv),]
        return new_urls+urls
    
    def upload_csv(self,request):
        if request.method=='POST':
            csv_file=request.FILES["csv_upload"]
            file_data=csv_file.read().decode('utf-8')
            csv_data=file_data.split('\n')
            for x in csv_data:
                if x:
                    fields=x.split(',')
                    created=Content.objects.update_or_create(
                        name=fields[0],
                        type=fields[1],
                        pic=fields[2],
                        des=fields[3],
                        rate=fields[4],
                        link=fields[5]
                    )
        form=CsvImportForm()
        data={'form':form}
        return render(request,'admin/csv_upload.html',data)


class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','type','message')

class UserAdmin(admin.ModelAdmin):
    list_display=('name','password','products')

admin.site.register(Webpage,WebpageAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(User,UserAdmin)
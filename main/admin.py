from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from rest_framework.exceptions import ValidationError

from main.models import *


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    def clean(self):
        if len(self.cleaned_data.get("colors")) >= 8:
            raise ValidationError(" Вы можете выбрать не больше восьми изображений")

    class Meta:
        model = Product
        fields = "__all__"


class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    extra = 1

    max_num = 8
    min_num = 0


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    inlines = [ProductImagesInline]


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


class AboutUsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = AboutUs
        fields = "__all__"


class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm


class PublicOfferAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = PublicOffer
        fields = "__all__"


class PublicOfferAdmin(admin.ModelAdmin):
    form = PublicOfferAdminForm


@admin.register(CallbackRequest)
class CallbackRequest(admin.ModelAdmin):
    readonly_fields = ("type_of_appeal", )
    search_fields = ("name", "number")
    list_display = ("name", "number")
    list_filter = ("did_callback", )


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
admin.site.register(Color)
admin.site.register(News, NewsAdmin)
admin.site.register(Help)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(PublicOffer, PublicOfferAdmin)
admin.site.register(OurContacts)
admin.site.register(Slider)
admin.site.register(OurAdvantages)
admin.site.register(Footer)
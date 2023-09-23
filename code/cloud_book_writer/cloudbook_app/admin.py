# from django.contrib import admin
# from django.urls import reverse
# from django.utils.html import format_html
# from .models import Document

# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'view_document_link')
#     search_fields = ('title',)

#     def view_document_link(self, obj):
#         if obj.file:
#             return format_html(f'<a href="{obj.file.url}" target="_blank">View</a>')
#         else:
#             return "No document file"

#     view_document_link.short_description = 'Document'

# admin.site.register(Document, DocumentAdmin)



from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Document
from tinymce.widgets import TinyMCE
from django import forms
from django.db import models


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file', 'content')

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
    list_display = ('title', 'view_document_link')
    search_fields = ('title',)

    def view_document_link(self, obj):
        if obj.file:
            return format_html(f'<a href="{obj.file.url}" target="_blank">View</a>')
        else:
            return "No document file"

    view_document_link.short_description = 'Document'

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(Document, DocumentAdmin)

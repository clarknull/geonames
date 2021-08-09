from django.contrib import admin
from django.apps import apps
from . import models

# Register your models here.

app = apps.get_app_config('user')
for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (admin.ModelAdmin,), {})

    model_admin.list_display_links = model.admin_list_display_links if hasattr(model,
                                                                               'admin_list_display_links') else ()
    model_admin.list_editable = model.admin_list_editable if hasattr(model, 'admin_list_editable') else ()
    model_admin.search_fields = model.admin_search_fields if hasattr(model, 'admin_search_fields') else ()

    admin.site.register(model, model_admin)
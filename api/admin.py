from django.contrib import admin
from django.apps import apps
from . import models

# Register your models here.

app = apps.get_app_config('api')
for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (admin.ModelAdmin,), {})
    if hasattr(model, 'Admin'):
        for attr, value in model.Admin.__dict__.items():
            if hasattr(model_admin, attr) and attr[:2] != '__':
                setattr(model_admin, attr, value)
    admin.site.register(model, model_admin)

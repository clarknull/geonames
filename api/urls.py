from django.urls import path

from . import views


urlpatterns = [
    # path('countries/', views.LocationGet.as_view(), name='countries'),
    path('state/<str:code>', views.GetChildren.as_view(level=2), name='state'),
    path('city/<str:code>', views.GetChildren.as_view(level=3), name='cities'),
    path('details/<str:code>', views.Details.as_view(), name='details'),

]
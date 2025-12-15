from django.urls import path
from .views import R2View, R3View

urlpatterns = [
    path("r2/", R2View.as_view(), name="R2"),
    path("r2/", R3View.as_view(), name="R3"),
]

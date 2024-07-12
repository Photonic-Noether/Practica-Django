from django.urls import path
import weather.views as views

urlpatterns = [
    path("", views.widget_tiempo),
    path("persona", views.ver_personas)
]

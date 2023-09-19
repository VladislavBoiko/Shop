from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

app_name = "orders"

urlpatterns = [
    # http://127.0.0.1:8000/users/
    path("orders/", order, name="order"),

]

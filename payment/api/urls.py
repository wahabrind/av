
from django.urls import path,include
from . import views
urlpatterns = [
    path('make-payment/', views.MakePayment.as_view(),name="make_payment"),
]

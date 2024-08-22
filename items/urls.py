from django.urls import path
from items import views
urlpatterns=[
    path("mobile/<int:pid>",views.mobile,name="ms"),
    path("laptop/<int:pid>",views.laptop,name="lp"),
    path("airpod/<int:pid>",views.laptop,name="ap"),
]
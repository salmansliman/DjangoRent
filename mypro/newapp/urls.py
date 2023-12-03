from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index" ),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>',views.uprec,name="uprec"),
    path('addC/',views.addC,name="addC"),
    path("addCrec/",views.addCrec,name="addCrec"),
    path('deleteC/<int:id>',views.deleteC,name="deleteC"),
    path('updateC/<int:id>/',views.updateC,name="updateC"),
    path('updateC/upCrec/<int:id>',views.upCrec,name="upCrec"),
    path('rent/',views.rent,name="rent"),
    path("addRent/",views.addRent,name="addRent"),
    path('deleteR/<int:id_rent>/',views.deleteR,name="deleteR"),
    


    

]
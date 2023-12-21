"""
URL configuration for pharmacy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start),
    path('reg',views.reg),
    path('Login',views.Login),
    path('pharmahome',views.pharmahome),
    path('userhome',views.userhome),
    path('pharmaprofile',views.pharmaprofile),
    path('edit_pharmaprofile/<int:id>',views.edit_pharmaprofile,name='edit_pharmaprofile'),
    path('pharmacyhome',views.pharmacyhome),
    path('userprofile',views.userprofile),
    path('edit_userprofile/<int:id>',views.edit_userprofile,name='edit_userprofile'),
    path('Logout',views.Logout),
    path('addproduct',views.addproduct),
    path('viewproduct',views.viewproduct),
    path('deleteproduct<int:id>',views.deleteproduct,name='deleteproduct'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),
    path('userviewproduct',views.userviewproduct),
    path('Add_cart/<int:id>',views.Add_cart,name='Add_cart'),
    path('erro404',views.erro404),
    path('success',views.success),
    path('dummypay',views.dummypay),
    path('buymedicine/<int:id>',views.buymedicine,name='buymedicine'),
    path('cartdlt/<int:id>',views.cartdlt,name='cartdlt'),
    path('viewcart',views.viewcart,name='viewcart'),
    path('userhistory',views.userhistory),
    path('pharmahistory',views.pharmahistory),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

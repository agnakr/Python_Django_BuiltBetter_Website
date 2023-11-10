from django.urls import path
from.import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('contact_view',views.contact_view,name='contact_view'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('registerview', views.registerview, name='registerview'),
]
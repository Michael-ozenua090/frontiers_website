from django.urls import path
from.views import index, about, contact, faq

urlpatterns = [
   path('', index),
   path('about-us', about),
   path('contact-us', contact),
   path('faq', faq),

]

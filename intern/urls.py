from django.urls import path, include

from intern import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('contact', views.contact, name='contact'),
    path('book', views.book, name='book'),
    path('signout', views.signout, name='signout'),
    path('postadd', views.postadd, name='postadd'),
    path('showadd', views.showadd, name='showadd'),
]

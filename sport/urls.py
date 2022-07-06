from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('app/', views.app, name = "app"),
    path('twitter/', views.twitter, name = "twitter"),
    path('facebook/', views.facebook, name = "facebook"),
    path('history/', views.results, name = "history"),
    path('jackpot/', views.jackpot, name = "jackpot"),
    path('payment/', views.payment, name = "payment"),
    path('pricing/', views.price, name = "price"),
    path('viptips/', views.viptips, name = "viptips"),
    path('signup/', views.signup, name = "signup"),
    path('singlebet/', views.singlebet, name = "singlebet"),
    path('viptipsgames/', views.viptipsgames, name = "viptips"),
    path('accounts/', include('django.contrib.auth.urls')),
]

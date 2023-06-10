from django.urls import path,include
from . import views
urlpatterns=[
    path('men_shirts/',views.MenShirts,name="MenShirt"),
    path('men_shirts/<int:id>/',views.MenShirt,name="MenShirt"),
    path('men_jackets/',views.MenJackets,name="MenJackets"),
    path('men_jackets/<int:id>/',views.MenJacket,name="MenJacket"),
    path('men_pants/',views.MenPants,name="MenPants"),
    path('men_pants/<int:id>/',views.MenPant,name="MenPant"),
    path('men_joggers/',views.MenJoggers,name="MenJoggers"),
    path('men_joggers/<int:id>/',views.MenJogger,name="MenJogger"),
    path('glasses/',views.glasses,name="Glasses"),
    path('glasses/<int:id>/',views.glass,name="Glass"),
    path('earrings/',views.earrings,name="Earrings"),
    path('earrings/<int:id>/',views.earring,name="Earring"),
    path('necklaces/',views.necklaces,name="Necklaces"),
    path('necklaces/<int:id>/',views.necklace,name="Necklace"),
    path('women_shirts/',views.WomenShirts,name="WomenShirts"),
    path('women_shirts/<int:id>/',views.WomenShirt,name="WomenShirt"),
    path('women_jackets/',views.WomenJackets,name="WomenJackets"),
    path('women_jackets/<int:id>/',views.WomenJacket,name="WomenJacket"),
    path('women_pants/',views.WomenPants,name="WomenPants"),
    path('women_pants/<int:id>/',views.WomenPant,name="WomenPant"),
    path('women_joggers/',views.WomenJoggers,name="WomenJoggers"),
    path('women_joggers/<int:id>/',views.WomenJogger,name="WomenJogger")
]
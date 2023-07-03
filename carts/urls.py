from django.urls import path,include
from . import views
urlpatterns = [
    path('carts/<int:id>/',views.carts,name='Cart'),
    path('carts/<int:id>/_womenshirt/<int:womenshirts_id>/',views.adc_womenshirts),
    path('carts/<int:id>/women_shirts/',views.get_womenshirts),
    path('carts/<int:id>/_womenpant/<int:womenpants_id>/',views.adc_womenpants),
    path('carts/<int:id>/women_pants/',views.get_womenpants),
    path('carts/<int:id>/_womenjacket/<int:womenjackets_id>/',views.adc_womenjackets),
    path('carts/<int:id>/women_jackets/',views.get_womenjackets),
    path('carts/<int:id>/_womenjogger/<int:womenjoggers_id>/',views.adc_womenjoggers),
    path('carts/<int:id>/women_joggers/',views.get_womenjoggers),
    path('carts/<int:id>/_necklace/<int:necklaces_id>/',views.adc_necklaces),
    path('carts/<int:id>/necklaces/',views.get_necklaces),
    path('carts/<int:id>/_glass/<int:glasses_id>/',views.adc_glasses),
    path('carts/<int:id>/glasses/',views.get_glasses),
    path('carts/<int:id>/_earring/<int:earrings_id>/',views.adc_earrings),
    path('carts/<int:id>/earrings/',views.get_earrings),
    path('carts/<int:id>/_menshirt/<int:menshirts_id>/',views.adc_menshirts),
    path('carts/<int:id>/men_shirts/',views.get_menshirts),
    path('carts/<int:id>/_menpant/<int:menpants_id>/',views.adc_menpants),
    path('carts/<int:id>/men_pants/',views.get_menpants),
    path('carts/<int:id>/_menjogger/<int:menjoggers_id>/',views.adc_menjoggers),
    path('carts/<int:id>/men_joggers/',views.get_menjoggers),
    path('carts/<int:id>/_menjacket/<int:menjackets_id>/',views.adc_menjackets),
    path('carts/<int:id>/men_jackets/',views.get_menjackets)
]
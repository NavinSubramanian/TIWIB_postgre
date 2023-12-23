from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name="homepage"),
    path('home/',views.index),
    path('inf',views.index),
    path('men/',views.men),
    path('movie/',views.movie),
    path('women/',views.women),
    path('dad/',views.dad),
    path('mom/',views.mom),
    path('kids/',views.kids),
    path('teenboys/',views.teenboys),
    path('teengirls/',views.teengirls),
    path('boyfriend/',views.boyfriend),
    path('girlfriend/',views.girlfriend),
    path('fathersday/',views.fathersday),
    path('mothersday/',views.mothersday),
    path('valentinesday/',views.valentinesday),
    path('aniversary/',views.aniversary),
    path('birthdaygift/',views.birthdaygift),
    path('graduation/',views.graduation),
    path('engagement/',views.engagement),
    path('wedding/',views.wedding),
    path('funny/',views.funny),
    path('gaggifts/',views.gaggifts),
    path('geek/',views.geek),
    # path('starwars/',views.starwars),
    path('anime/',views.anime),
    path('gamers/',views.gamers),
    path('travel/',views.travel),
    path('food/',views.food),
    path('allgiftsguide/',views.allgiftsguide),
    path('allgiftsguide/<str:genre>/',views.creation),
    path('submitaproduct/',views.submitaproduct),
    path('meme/',views.meme),
    path('stupendous/',views.stupendous),
    path('kitchen/',views.kitchen),
    path('knockout/',views.knockout),
    path('neutral/',views.neutral),
    path('<str:genre>/filter',views.filter),
    path('products/<int:item>',views.seperateprd),
    path('funnyperson/',views.funnyperson),
    path('contactus/',views.contactus),
    path('<str:genre>/check',views.check),
    path('check',views.check),
    path('<str:genre>/register',views.register),
    path('register',views.register),
    path('search',views.search),
    path('<str:genre>/search', views.search),
    path('<str:genre>/logins',views.logins),
    path('<str:genre>/logout',views.logout),
    path('logout',views.logout),
    # path('successlogin',views.successlogin),
    path('logins',views.logins),
    path('<str:genre>/alogin/',views.alogins),
    path('<str:genre>/savedproducts',views.savedproducts),
    path('unsavedproducts',views.unsavedproducts),
    path('<str:genre>/unsavedproducts',views.unsavedproducts),
    path('createblog/', views.create_blog, name='createblog'),
    # path('success/', views.success_page, name='success_page'),
]
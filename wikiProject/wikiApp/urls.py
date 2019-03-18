from django.urls import path
from .import views



urlpatterns=[

    # path('',views.allpost,name='index'),
    path('',views.index,name='index'),
    path('remake/',views.create,name='create'),
    path('allpost/',views.allpost,name='allpost'),
    # path('relateditems',views.relateditems,name='relateditems'),
    path('addentry/',views.newentry,name='newentry'),
    path('update_related/<str:id>',views.update,name='update'),
    path('delete_related/<str:id>',views.delete,name='delete'),
    path('logout/',views.logout,name='logout'),
    path('newrelative/',views.newrelative,name='newrelative'),
    path('details/<int:wikiPostID>/',views.details,name='details'),
    # path('login/',views.login,name='login'),
    # path('update_wiki/',views.updatewiki,name='updatewiki'),

    # path('')



]
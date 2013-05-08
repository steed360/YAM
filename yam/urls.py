from django.conf.urls import patterns, include, url
import  yam.views 

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def writeStringFN (x):  
    from django.http import HttpResponse
    return HttpResponse ("welcome")

urlpatterns = patterns('',
    ('^$', writeStringFN  ),
    ('^recipe_ingredients/(\d+)/$', yam.views.recipeIngredients),
    ('^add_ingredient/(\d+)/$', yam.views.addIngredient),
    ('^add/$', yam.views.saveNewIngredient),
    ('^hello/$', yam.views.hello),
    ('^time/$', yam.views.time),
    (r'^time/plus/(\d{1,2})/$', yam.views.hoursAhead),

    # Examples:
    # url(r'^$', 'yam.views.home', name='home'),
    # url(r'^yam/', include('yam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

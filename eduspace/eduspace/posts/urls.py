from django.conf.urls import url
from django.contrib import admin
from posts import views
#from posts import views
#(
#	home,
#	aboutus,
#	committe,
#	login,
#	)

urlpatterns = [
	url(r'^$', views.home, name="home"),
    #url(r'^aboutus/', views.aboutus, name="aboutus"),
    #url(r'^committe/', views.committe,name="committe"),
    #url(r'^activity/', views.activity, name="activity"),
    #url(r'^login/', views.login, name="login"),
    #url(r'^posts/$', "<appname>.views.<function_name>"),  
    url(r'^physics/(?P<sub_id>[0-9]+)$', views.physics, name = "physics"),
    url(r'^chemistry/$', views.chemistry, name = "chemistry"),
    
    url(r'^physics/topic_id/(?P<explain_id>[0-9]+)$', views.indv_expl, name = "description"),

]
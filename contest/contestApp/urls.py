"""contest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

# For Function views
#from . import views

# For Class bases views
from .views import IndexView, Pagina2View, Pagina3View, Pagina4View


urlpatterns = [
    # Function view
    # url(r'^$', views.index, name='index')
    # Class based biew
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^pagina2/$', Pagina2View.as_view(), name='pagina2'),
    url(r'^pagina3/$', Pagina3View.as_view(), name='pagina3'),
    url(r'^pagina4/$', Pagina4View.as_view(), name='pagina4'),
]

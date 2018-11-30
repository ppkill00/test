"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from dashing.utils import router
from django.views.generic.base import RedirectView

from .widgets import CustomDashboard, MyCustomWidget
from rest_framework import routers
from apiv1 import views

from dashboard.views import index, gentella_html


router = routers.DefaultRouter()
router.register(r'alertSystem', views.AlertViewSet)

dashing_patterns = [
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index'),
    url(r'dashboard/$', CustomDashboard.as_view()),
    url(r'dashboard/widgets/new_users_widget/', MyCustomWidget.as_view(), name='widget_new_users_widget'),
]
 
api_patterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

dashboard_patterns = [
    url(r'^$', index, name='index'),
    url(r'^.*\.html', gentella_html, name='gentella'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dashing/', include(dashing_patterns), name='dashing_patterns'),
    url(r'^apiv1/', include(api_patterns), name='api_patterns'),
    url(r'^dashboard/', include(dashboard_patterns), name='dashboard_patterns'),
]
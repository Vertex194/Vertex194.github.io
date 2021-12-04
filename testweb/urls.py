"""testweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include,url
from myapp.views import homepage,showpost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage),
    path('post/<slug:slug>/',showpost),
    # #新增應用程式網站
    # path('myapp/',include('myapp.urls')),
    # string前面加上'r'表示是個raw string,不要轉意backslash'\'由於正則表示式和\會有衝突使用了正則表示式後
    # url(r'^home/',homepage),
    url(r'^$',homepage),
    url(r'^admin/',admin.site.urls),
    
]

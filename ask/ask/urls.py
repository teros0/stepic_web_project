from django.conf.urls import url, include
from django.contrib import admin
from ask.views import post_list, popular, ask, signup, logine
from qa.views import test, question

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list),
    url(r'^login/', logine),
    url(r'^signup/', signup),
    url(r'^question/', include('qa.urls')),
    url(r'^ask/', ask),
    url(r'^popular/', popular),
    url(r'^new/', test),
]



"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
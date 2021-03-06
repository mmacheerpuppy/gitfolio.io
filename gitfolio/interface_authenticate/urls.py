from django.conf.urls import url
from django.urls import include

from interface_authenticate import views

app_name = 'interface_authenticate'

# For the example in this implementation to work you must include this in your urls.py url(r'^oauth/',
# include('social_django.urls', namespace='social')), since this application is used in conjunction with the
# social_django packages. Otherwise feel free to ignore this.

urlpatterns = [
    # Calls login view to log the user in. Calls logout view to log the user out
    url(r'^$', views.LoginAuthHandler.as_view(), name='login'),
    url(r'^logout$', views.LogoutAuthHandler.as_view(), name='logout'),
]

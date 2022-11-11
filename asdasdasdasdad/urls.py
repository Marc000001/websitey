from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from accounts.views import login_page, home_page, logout, register_page, updateUser, deleteUser, user_list

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('admin/', admin.site.urls),
    path('staff/', include("staff.urls")),
    path('users/', user_list, name='users'),
    path('logout/', logout, name='logout'),
    path('register/', register_page, name='register'),

    path('updateUser/<int:pk>/', updateUser, name='updateUser'),
    path('deleteUser/<int:pk>/', deleteUser, name='deleteUser'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

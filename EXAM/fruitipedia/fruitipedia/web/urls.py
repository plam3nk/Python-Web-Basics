from django.urls import path, include

from fruitipedia.web.views import index, dashboard, fruit_create, fruit_details, fruit_edit, fruit_delete, \
    profile_create, profile_details, profile_edit, profile_delete

urlpatterns = (
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', fruit_create, name='fruit create'),
    path('<int:pk>/details/', fruit_details, name='fruit details'),
    path('<int:pk>/edit/', fruit_edit, name='fruit edit'),
    path('<int:pk>/delete/', fruit_delete, name='fruit delete'),
    path('profile/', include([
        path('create/', profile_create, name='profile_create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
)
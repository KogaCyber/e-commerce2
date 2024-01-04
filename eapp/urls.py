from django.urls import path

from eapp.views import index, indexItem, add_item, update_item,delete_item

app_name = 'eapp'
urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', indexItem, name='detail'),
    path("additem/", add_item, name='add_item'),
    path("updateitem/<int:my_id>/", update_item, name='update_item'),
    path("delete/<int:my_id>/", delete_item, name='delete_item'),
]

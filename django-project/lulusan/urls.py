from django.urls import path
from .views import ( 
    LulusanCreateView,
    LulusanListView,
    LulusanDetailView,
    LulusanUpdateView,
    LulusanDeleteView,
    create,
    delete,
)

app_name = 'lulusan'
urlpatterns = [
    path('delete/<int:delete_id>/', delete, name='delete'),
    path('update/<int:pk>/', LulusanUpdateView.as_view(), name='update'),
    path('create/', create, name='create'),
    path('detail/<slug:slug>/', LulusanDetailView.as_view(), name='detail'),
    path('list/', LulusanListView.as_view(), name='list'),
]

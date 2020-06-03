from django.urls import path
from .views import ( 
    LulusanCreateView,
    LulusanListView,
    LulusanDetailView,
    LulusanUpdateView,
    LulusanDeleteView,
)

app_name = 'lulusan'
urlpatterns = [
    path('delete/<int:pk>/', LulusanDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', LulusanUpdateView.as_view(), name='update'),
    path('create/', LulusanCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', LulusanDetailView.as_view(), name='detail'),
    path('list/', LulusanListView.as_view(), name='list'),
]

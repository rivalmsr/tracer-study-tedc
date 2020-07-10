from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ( 
    # LulusanCreateView,
    LulusanListView,
    LulusanDetailView,
    LulusanUpdateView,
    # LulusanDeleteView,
    create,
    delete,
)

app_name = 'lulusan'
urlpatterns = [
    path('delete/<int:delete_id>/', login_required(delete), name='delete'),
    path('update/<int:pk>/', login_required(LulusanUpdateView.as_view()), name='update'),
    path('create/', login_required(create), name='create'),
    path('detail/<slug:slug>/', login_required(LulusanDetailView.as_view()), name='detail'),
    path('list/', login_required(LulusanListView.as_view()), name='list'),
]

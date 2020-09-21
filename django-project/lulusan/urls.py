from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ( 
    # LulusanCreateView,
    LulusanListView,
    LulusanProfileView,
    LulusanUpdateView,
    # LulusanDeleteView,
    create,
    delete,
    activate_account,
    Index,
    LulusanUpdateBiodataView,
)

app_name = 'lulusan'
urlpatterns = [
    path('update-biodata/<int:pk>/', login_required(LulusanUpdateBiodataView.as_view()), name='update-biodata'),
    path('index/', Index.as_view()),
    path('activation/<str:uidb64>/<str:token>/', activate_account, name="activate" ),
    path('delete/<int:delete_id>/', login_required(delete), name='delete'),
    path('update/<int:pk>/', login_required(LulusanUpdateView.as_view()), name='update'),
    path('create/', login_required(create), name='create'),
    path('detail/<slug:slug>/', login_required(LulusanProfileView.as_view()), name='detail'),
    path('list/', login_required(LulusanListView.as_view()), name='list'),
]

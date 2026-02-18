from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListBookView.as_view(), name="books"),
  path('book', views.CreateBookView.as_view(), name="create_book"),
  path('book/<int:pk>', views.DetailBookView.as_view(), name="detail_book"),
  path('book/<int:pk>/update', views.UpdateBookView.as_view(), name="update_book"),
  
  path('api/book', views.CreateListBookAPIView.as_view()),
  path('api/book/<int:pk>', views.RetrieveUpdateDestroyBookApiView.as_view())
]
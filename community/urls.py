from django.urls import path
from community import views
# from user import User

app_name = 'community'

urlpatterns = [
    path('', views.board)
]

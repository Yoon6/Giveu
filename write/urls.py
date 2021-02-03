from django.contrib import admin
from django.urls import path
import write.views

urlpatterns = [
    path('', write.views.home, name='home'),
    path('create/', write.views.create, name='create'),
    path('detail/<int:post_id>', write.views.detail, name='detail'),
    path('delete/<int:post_id>', write.views.delete, name='delete'),
    path('update/<int:post_id>', write.views.update, name='update'),
]

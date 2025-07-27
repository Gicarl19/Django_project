from django.urls import path
from .views import index, lyrics, lyrics1, song_lyrics, student_list, enrollment, student_create, student_update, student_delete
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('lyrics', lyrics, name='lyrics'),
    path('song_lyrics', song_lyrics, name='song_lyrics'),
    path('enrollment', enrollment, name='enrollment'),
    path('lyrics1', lyrics1, name='lyrics1'),
    path('student_list/', student_list, name='student_list'),
    path('create/', student_create, name='student_create'),
    path('<int:pk>/update/', student_update, name='student_update'),
    path('<int:pk>/delete/', student_delete, name='student_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
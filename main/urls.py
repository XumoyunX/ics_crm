from django.urls import path, include
from main.views import index, course_list, blog_list

app_name="main"

urlpatterns = [
    path('', index, name='index'),
    path('clinet/', include('clinet.urls')),
    path('course/', course_list, name='course'),
    path('blog/', blog_list, name='blog')
]
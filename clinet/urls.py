from django.urls import path
from clinet import views




urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('category_list/', views.category_list, name="category_list"),
    path('category_create/', views.category_create, name="category_create"),
    path('<int:pk>category_edit/', views.category_edit, name="category_edit"),
    path('<int:pk>/category_delete/', views.category_delete, name="category_delete"),

    path('groups_list/', views.groups_list, name="groups_list"),
    path('groups_create/', views.groups_create, name="groups_create"),
    path('<int:pk>/groups_edit/', views.groups_edit, name="groups_edit"),
    path('<int:pk>/groups_delete/', views.groups_delete, name="groups_delete"),

    path('students_guruh/<int:id>/', views.students_guruh, name="students_guruh"),

    path('students_list/', views.students_list, name="students_list"),
    path('students_create/', views.students_create, name="students_create"),
    path('<int:pk>/students_edit/', views.students_edit, name="students_edit"),
    path('<int:pk>/students_delete/', views.students_delete, name="students_delete"),


    path('blog_list/', views.blog_list, name="blog_list"),
    path('blog_create/', views.blog_create, name="blog_create"),
    path('<int:pk>/blog_edit/', views.blog_edit, name="blog_edit"),
    path('<int:pk>/blog_delete/', views.blog_delete, name="blog_delete"),

    path('year_list/', views.year_list, name="year_list"),
    path('year_create/', views.year_create, name="year_create"),
    path('<int:pk>/year_edit/', views.year_edit, name="year_edit"),
    path('<int:pk>/year_delete/', views.year_delete, name="year_delete"),

    path('davomat_list/', views.davomat_list, name="davomat_list"),
    path('davomat_create/', views.davomat_create, name="davomat_create"),
    path('<int:pk>/davomat_edit/', views.davomat_edit, name="davomat_edit"),
    path('<int:pk>/davomat_delete/', views.davomat_delete, name="davomat_delete"),


    path('molya_list_molya/<int:id>/', views.molya_list_molya, name="molya_list_molya"),

    path('molya_list/', views.molya_list, name="molya_list"),
    path('molya_create/', views.molya_create, name="molya_create"),
    path('<int:pk>/molya_edit/', views.molya_edit, name="molya_edit"),
    path('<int:pk>/molya_delete/', views.molya_delete, name="molya_delete"),

    path('molya_fanta/<int:id>/', views.molya_fanta, name="molya_fanta"),

    path('molya_fanta_list/', views.molya_fanta_list, name="molya_fanta_list"),
    path('molya_fanta_create/', views.molya_fanta_create, name="molya_fanta_create"),
    path('<int:pk>/molya_fanta_edit/', views.molya_fanta_edit, name="molya_fanta_edit"),
    path('<int:pk>/molya_fanta_delete/', views.molya_fanta_delete, name="molya_fanta_delete")

]

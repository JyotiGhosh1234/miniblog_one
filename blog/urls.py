from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='Homepage' ),
    path('about/', views.about, name='Aboutpage' ),
    path('contact/', views.contact, name='Contactpage' ),
    path('dashboard/', views.dashboard, name='Dashboardpage' ),
    path('logout/', views.user_logout, name='Logoutpage' ),
    path('signup/', views.user_signup, name='Signuppage' ),
    path('login/', views.user_login, name='Loginpage' ),

    path('addpost/', views.add_post, name='Addpost' ),
    path('editpost/<int:id>/', views.edit_post, name='Editpost' ),
    path('deletepost/<int:id>/', views.delete_post, name='Deletepost' ),
]